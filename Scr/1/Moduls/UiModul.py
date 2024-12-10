import tkinter as tk
from PIL import ImageTk

class UI:
    def __init__(self, root):
        # Кнопки
        self.load_button = tk.Button(root, text="Загрузить изображение")
        self.load_button.grid(row=0, column=0, padx=10, pady=10)

        self.resize_button = tk.Button(root, text="Изменить размер")
        self.resize_button.grid(row=1, column=0, padx=10, pady=10)

        # Блок информации
        self.info_label = tk.Label(root, text="Информация об изображении:")
        self.info_label.grid(row=2, column=0, padx=10, pady=10)

        self.info_text = tk.Text(root, width=40, height=10)
        self.info_text.grid(row=3, column=0, padx=20, pady=20)

        # Область для отображения изображения
        self.image_label = tk.Label(root)
        self.image_label.grid(row=0, column=1, rowspan=4)

    def display_image(self, img):
        img.thumbnail((400, 400))
        self.tk_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def update_info(self, image_path, size):
        self.info_text.delete(1.0, tk.END)
        if image_path:
            width, height = size
            self.info_text.insert(tk.END, f"Файл: {image_path}\\n")
            self.info_text.insert(tk.END, f"Размер: {width}x{height}")
        else:
            self.info_text.insert(tk.END, "Изображение не загружено")
