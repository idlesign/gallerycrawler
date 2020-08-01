from bs4 import BeautifulSoup

from gallerycrawler.toolbox import Crawler, PageDetails, dump, setup_logging


class WaralbumCrawler(Crawler):

    selector_listing_next: str = '.wp-pagenavi .nextpostslink'
    selector_details: str = '#archive .clearfloat a'
    selector_details_img_small: str = '.entry img'

    def _get_details(self, page_details: BeautifulSoup) -> PageDetails:

        get_href = self._get_href

        title = page_details.select_one('meta[property="og:title"]').attrs['content']
        img_small = self._get_details_img_small(page_details)

        img_author = ''
        img_orig = ''

        for tag in page_details.select('div .related-list li'):
            css = tag.attrs.get('class', {})
            tag_text = tag.text

            if 'yapb_alternative_format' in css:
                img_orig = get_href(tag.contents[0])
                assert 'http' in img_orig, f'Bogus original image link: {img_orig}'

            elif tag_text.lower().startswith('автор'):
                img_author = tag_text

        details = PageDetails(
            title=title,
            img_author=img_author,
            img_orig=img_orig,
            img_small=img_small,
        )

        return details


if __name__ == '__main__':

    import logging
    setup_logging(logging.DEBUG)

    dump(
        crawler=WaralbumCrawler,
        url='https://waralbum.ru/?s=%D0%BD%D1%8E%D1%80%D0%BD%D0%B1%D0%B5%D1%80%D0%B3&x=0&y=0',
        fpath='waralbum.html'
    )
