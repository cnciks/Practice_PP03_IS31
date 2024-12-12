import sys
import time
from tkinter import filedialog, messagebox
from PIL import Image

class ImageHandler:
    def __init__(self):
        self.path1 = ""
        self.path2 = ""

    def load_image(self, image_number):
        start_time = time.time()
        path = filedialog.askopenfilename(
            title="Выберите изображение", 
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )

        if path:
            if image_number == 1:
                self.path1 = path
            elif image_number == 2:
                self.path2 = path
            load_time = time.time() - start_time
            return path, load_time

        return None, None

    def resize_and_concatenate(self, width, height):
        try:
            start_time = time.time()
            img1 = Image.open(self.path1)
            img2 = Image.open(self.path2)

            original_size1 = img1.size
            original_size2 = img2.size

            img1 = img1.resize((width, height))
            img2 = img2.resize((width, height))

            result_img = Image.new('RGB', (width * 2, height))
            result_img.paste(img1, (0, 0))
            result_img.paste(img2, (width, 0))

            output_path = self.path1.rsplit('/', 1)[0] + '/concatenated_image.jpg'
            result_img.save(output_path)

            resize_time = time.time() - start_time

            result_info = {
                'original_size1': original_size1,
                'original_size2': original_size2,
                'output_path': output_path,
                'resize_time': resize_time
            }
            return result_info, result_img

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            return None, None
