import logging
from typing import Set, Generator, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
from requests import Session

from .page_details import PageDetails

LOGGER = logging.getLogger(__name__)


class Crawler:

    selector_listing_next: str = '.next'
    selector_details: str = '.details'
    selector_details_title: str = 'h1'
    selector_details_img: str = 'img'
    selector_details_img_small: str = '.thumbnail'
    selector_details_author: str = '.author'

    def __init__(self, url: str):
        self.url = url

        LOGGER.info(f'Start crawling from: {url} ...')

        session = Session()
        session.headers = {
            'User-Agent': (
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/79.0.3945.136 YaBrowser/20.2.3.320 (beta) Yowser/2.5 Safari/537.36'
            )
        }
        self.session = session

    def _get_response(self, url: str) -> BeautifulSoup:
        response = self.session.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, features='lxml')

    def _get_href(self, element: Optional[Tag]) -> str:

        if element:
            return element.attrs['href'].partition('#')[0]

        return ''

    def _get_text(self, element: Optional[Tag]) -> str:

        if element:
            return element.text.strip()

        return ''

    def _get_src(self, element: Optional[Tag]) -> str:

        if element:
            return element.attrs['src']

        return ''

    def _get_img_url(self, element: Optional[Tag]) -> str:

        if element:
            if element.name == 'img':
                return self._get_src(element)
            return self._get_href(element)

        return ''

    def _get_page_details_links(self, page_listing: BeautifulSoup) -> Set[str]:

        pages_details_links = []

        for link in page_listing.select(self.selector_details):
            link = self._get_href(link)

            if link:
                pages_details_links.append(link)

        return set(pages_details_links)

    def _get_details_title(self, page: BeautifulSoup) -> str:
        return self._get_text(page.select_one(self.selector_details_title))

    def _get_details_author(self, page: BeautifulSoup) -> str:
        return self._get_text(page.select_one(self.selector_details_author))

    def _get_details_img(self, page: BeautifulSoup) -> str:
        return self._get_img_url(page.select_one(self.selector_details_img))

    def _get_details_img_small(self, page: BeautifulSoup) -> str:
        return self._get_img_url(page.select_one(self.selector_details_img_small))

    def _get_details(self, page_details: BeautifulSoup) -> PageDetails:

        title = self._get_details_title(page_details)
        img_small = self._get_details_img_small(page_details)
        img_orig = self._get_details_img(page_details)
        img_author = self._get_details_author(page_details)

        img_small = img_small or img_orig
        img_orig = img_orig or img_small

        details = PageDetails(
            title=title,
            img_author=img_author,
            img_orig=img_orig,
            img_small=img_small,
        )

        return details

    def _get_page_listing_next_link(self, page_listing: BeautifulSoup) -> str:
        return self._get_href(page_listing.select_one(self.selector_listing_next))

    def _walk(self, url: str) -> Generator[PageDetails, None, None]:

        get = self._get_response
        get_details = self._get_details

        page_listing = get(url)

        for page_details_link in self._get_page_details_links(page_listing):
            page_details_link = urljoin(url, page_details_link)

            LOGGER.debug(f'Processing details page: {page_details_link} ...')

            page_details = get(page_details_link)

            details = get_details(page_details)
            details.url = page_details_link

            for attr in {'img_orig', 'img_small'}:
                val = getattr(details, attr)
                setattr(details, attr, urljoin(page_details_link, val))

            yield details

        page_next_link = self._get_page_listing_next_link(page_listing)

        if page_next_link:
            page_next_link = urljoin(url, page_next_link)
            LOGGER.debug(f'Processing next listing page: {page_next_link} ...')
            yield from self._walk(page_next_link)

    def results(self) -> Generator[PageDetails, None, None]:
        yield from self._walk(self.url)
