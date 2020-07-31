
class PageDetails:

    def __init__(
            self,
            *,
            title: str,
            img_author: str,
            img_orig: str,
            img_small: str,
            url: str = ''
    ):
        self.title = title
        self.img_author = img_author
        self.img_orig = img_orig
        self.img_small = img_small
        self.url = url

    def __str__(self):
        return self.url
