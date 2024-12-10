from tkinter import filedialog, messagebox
from PIL import Image

class ImageHandler:
    def __init__(self):
        self.path1 = ""
        self.path2 = ""

    def load_image(self, image_number):
        path = filedialog.askopenfilename(
            title="Выберите изображение", 
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if path:
            if image_number == 1:
                self.path1 = path
            elif image_number == 2:
                self.path2 = path
            return path
        return None

    def resize_and_concatenate(self, width, height):
        try:
            img1 = Image.open(self.path1).resize((width, height))
            img2 = Image.open(self.path2).resize((width, height))

            result_img = Image.new('RGB', (width * 2, height))
            result_img.paste(img1, (0, 0))
            result_img.paste(img2, (width, 0))

            output_path = self.path1.rsplit('/', 1)[0] + '/concatenated_image.jpg'
            result_img.save(output_path)

            return output_path, result_img
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            return None, None
