from gallerycrawler.toolbox import Crawler, dump, setup_logging


class NurnRusarchCrawler(Crawler):

    selector_listing_next: str = '.pager-next a'
    selector_details: str = '.field-content a'
    selector_details_title: str = '.field-name-field-full-title'
    selector_details_img: str = '.field-name-field-image a'
    selector_details_img_small: str = '.colorbox img'
    selector_details_author: str = '.field-name-field-authors .field-item'


if __name__ == '__main__':

    import logging
    setup_logging(logging.DEBUG)

    dump(
        crawler=NurnRusarchCrawler,
        url='http://nurnberg.rusarchives.ru/documents-list?field_archive_tid=All&field_full_title_value=&field_carrier_tid=40&field_date_sort_value%5Bvalue%5D%5Bdate%5D=&field_date_sort_value2%5Bvalue%5D%5Bdate%5D=',
        fpath='nurnrusarch.html'
    )
