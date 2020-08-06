
class PageDetails:

    def __init__(
            self,
            *,
            title: str,
            img_author: str,
            img_orig: str,
            thumbnail: str,
            url: str = ''
    ):
        self.title = title
        self.img_author = img_author
        self.img_orig = img_orig
        self.thumbnail = thumbnail
        self.url = url

    def __str__(self):
        return self.url
