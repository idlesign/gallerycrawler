from gallerycrawler.toolbox import Crawler, dump, setup_logging


class TrumanCrawler(Crawler):

    selector_listing_next: str = '.pager__item--next a'
    selector_details: str = '.search-result-item a'
    selector_details_title: str = '.page-title'
    selector_details_img: str = '.img-skin img'
    selector_details_author: str = '.field--name-field-source-photographer'


if __name__ == '__main__':

    import logging
    setup_logging(logging.DEBUG)

    dump(
        crawler=TrumanCrawler,
        url='https://www.trumanlibrary.gov/search?keys=nurnberg&op=Search&types%5Bphotograph_record%5D=photograph_record',
        fpath='truman.html',
    )
