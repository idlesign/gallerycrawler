from pathlib import Path
from typing import Type, Union

from .crawler import Crawler  # noqa
from .exporter import HtmlExporter  # noqa
from .page_details import PageDetails  # noqa
from .utils import setup_logging  # noqa


def dump(
        *,
        crawler: Type['Crawler'],
        url: str,
        fpath: Union[str, Path],
        probe: bool = False
):

    crawler = crawler(url, probe=probe)

    pages = []

    for idx, page in enumerate(crawler.results(), 1):
        pages.append(page)

    fpath = Path(fpath).absolute()

    exporter = HtmlExporter(pages)
    exporter.save(fpath)
