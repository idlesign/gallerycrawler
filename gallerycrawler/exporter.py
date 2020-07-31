from typing import List

from .page_details import PageDetails


class HtmlExporter:

    def __init__(self, pages: List[PageDetails]):
        self.pages = pages

    def save(self, fpath: str):

        lines = []

        for idx, page in enumerate(self.pages):
            author = page.img_author

            btn_copy = (
                '<button class="btn btn-sm btn-outline-secondary copier" '
                f'data-clipboard-target="#author-{idx}">c</button></td>')

            lines.append(
                '<tr>'
                f'<td><a href="{page.url}">{page.title}</a></td>'
                '<td>'
                f'<div id="author-{idx}">{author}</div>'
                f"{btn_copy if author else ''}"
                f'<td><a href="{page.img_orig}">'
                f'<img src="{page.img_small}" class="img-thumbnail" width="300"></a></td>'
                '</tr>'
            )

        compiled = TPL.replace('{rows}', '\n'.join(lines))

        with open(fpath, 'w') as f:
            f.write(compiled)


TPL = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.4/clipboard.min.js"></script>
    
    <title>gallerycrawler dump</title>
</head>
<body>

<div class="container">
    <div class="row">
        <div class="col">
            <table class="table table-striped table-bordered table-hover">
                {rows}
            </table>
        </div>
    </div>
</div>

<script>
    new ClipboardJS('.copier');
</script>

</body>
</html>
'''
