gallerycrawler
==============
https://github.com/idlesign/gallerycrawler

|release| |lic|

.. |release| image:: https://img.shields.io/pypi/v/gallerycrawler.svg
    :target: https://pypi.python.org/pypi/gallerycrawler

.. |lic| image:: https://img.shields.io/pypi/l/gallerycrawler.svg
    :target: https://pypi.python.org/pypi/gallerycrawler

Description
-----------

*Generic crawling for galleries*

1. Crawler starts from gallery listing URL;
2. It visits every details page mentioned on current listing page;
3. It gathers information from each details page;
4. It moves to the next listing URL.
5. Etc.

.. code-block:: python

    from galerycrawler.toolbox import Crawler, dump

    # Define crawler.
    class MyCrawler(Crawler):

        selector_listing_next: str = '.page-next a'
        selector_listing_thumbnails: str = '.thumbnail img'
        selector_details: str = '.page-details a'
        selector_details_title: str = '.page-title'
        selector_details_img: str = '.image img'
        selector_details_author: str = '.image-author'

    # Run dumping.
    dump(
        crawler=MyCrawler,
        url='https://mysite.some/gallery/',
        fpath='dumped.html'
    )
