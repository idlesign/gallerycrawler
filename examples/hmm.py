from gallerycrawler.toolbox import Crawler, dump, setup_logging


class HmmCrawler(Crawler):

    selector_listing_next: str = '.pagination li a[rel=next]'
    selector_listing_thumbnails: str = '.document-thumbnail img'
    selector_details: str = '.documentHeader a'
    selector_details_title: str = '#document h1[itemprop=name]'
    selector_details_img: str = '#document .gallery img'
    selector_details_author: str = '.blacklight-photographer.moreless'


if __name__ == '__main__':

    import logging
    setup_logging(logging.DEBUG)

    dump(
        crawler=HmmCrawler,
        url='https://collections.ushmm.org/search/?f%5Bf_cities%5D%5B%5D=Nuremberg&f%5Bf_images%5D%5B%5D=indiv_photographs&f%5Bf_key_event%5D%5B%5D=imt_nuremberg&per_page=50&q=nurnberg&search_field=Subjects+and+Keywords&sort=rg_number_sort+asc',
        fpath='hmm-photo.html',
    )

    dump(
        crawler=HmmCrawler,
        url='https://collections.ushmm.org/search/?f%5Bavailability%5D%5B%5D=digitized&f%5Bf_audiovisual%5D%5B%5D=historic_film&f%5Bf_cities%5D%5B%5D=Nuremberg&f%5Bf_key_event%5D%5B%5D=imt_nuremberg&per_page=50&q=nurnberg&search_field=Subjects+and+Keywords&sort=rg_number_sort+asc',
        fpath='hmm-video.html',
    )
