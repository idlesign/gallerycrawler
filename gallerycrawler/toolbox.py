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
        fpath: Union[str, Path] = '',
        probe: bool = False,
        show: bool = True,
):

    crawler_obj = crawler(url, probe=probe)

    pages = []

    for idx, page in enumerate(crawler_obj.results(), 1):
        pages.append(page)

    crawler_name = crawler.__name__

    if not fpath:
        fpath = f'{crawler_name}.html'

    fpath = Path(fpath).absolute()

    exporter = HtmlExporter(pages=pages, title=crawler_name)
    exporter.save(fpath)

    if show:
        import webbrowser
        webbrowser.open(f'file://{fpath}', new=2)
