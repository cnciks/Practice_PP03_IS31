from PIL import Image

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.image_path = None

    def load_image(self, path):
        if path:
            self.image_path = path
            self.image = Image.open(self.image_path)

    def resize_image(self, new_width, new_height):
        if self.image is not None:
            resized_image = self.image.resize((new_width, new_height), Image.LANCZOS)
            return resized_image
        return None
