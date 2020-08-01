from gallerycrawler.toolbox import Crawler, dump, setup_logging


class JacksonCrawler(Crawler):

    selector_listing_next: str = 'a.next'
    selector_details: str = '.as-heading a'
    selector_details_title: str = 'h1.pp-heading a'
    selector_details_img: str = '.a-image img'
    selector_details_author: str = 'p[itemprop=creator]'


if __name__ == '__main__':

    import logging
    setup_logging(logging.DEBUG)

    dump(
        crawler=JacksonCrawler,
        url='https://www.roberthjackson.org/collection/photos/',
        fpath='jackson.html'
    )
