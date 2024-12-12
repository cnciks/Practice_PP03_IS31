import time
import sys
from PIL import Image

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.image_path = None

    def load_image(self, path):
        start_time = time.time()
        if path:
            self.image_path = path
            self.image = Image.open(self.image_path)
            print(f"Image loaded in {time.time() - start_time:.6f} seconds.")
            print(f"Size of loaded image object: {sys.getsizeof(self.image)} bytes")
            print(f"Size of image path string: {sys.getsizeof(self.image_path)} bytes")

    def resize_image(self, new_width, new_height):
        start_time = time.time()
        if self.image is not None:
            resized_image = self.image.resize((new_width, new_height), Image.LANCZOS)
            print(f"Image resized in {time.time() - start_time:.6f} seconds.")
            print(f"Size of resized image object: {sys.getsizeof(resized_image)} bytes")
            return resized_image
        return None
