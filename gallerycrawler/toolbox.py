from typing import Type

from .crawler import Crawler  # noqa
from .exporter import HtmlExporter  # noqa
from .page_details import PageDetails  # noqa
from .utils import setup_logging  # noqa


def dump(*, crawler: Type['Crawler'], url: str, fpath: str):

    crawler = crawler(url)

    pages = []

    for idx, page in enumerate(crawler.results(), 1):
        pages.append(page)

    exporter = HtmlExporter(pages)
    exporter.save(fpath)
