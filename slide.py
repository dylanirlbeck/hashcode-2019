
class Slide:
    def __init__(self, image):
        if not image.horizontal:
            raise Exception("You must provide 2 vertical images or 1 horizontal image")
        self.image1 = image
        self.image2 = image

    def __init__(self, image1, image):
        if image.horizontal:
            raise Exception("You must provide 2 vertical images or 1 horizontal image")
        self.image1 = image1
        self.image2 = image2





class Image:
    def __init__(self, img_id, horizontal, img_tags):
        self._tags = _tags.union(img_tags)
        self._id = img_id
        self.horizontal = horizontal


