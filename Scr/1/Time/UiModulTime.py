import tkinter as tk
from PIL import ImageTk, Image
import time
import sys
from memory_profiler import memory_usage

class UI:
    def __init__(self, root):
        # Кнопки
        self.load_button = tk.Button(root, text="Загрузить изображение", command=self.load_image)
        self.load_button.grid(row=0, column=0, padx=10, pady=10)

        self.resize_button = tk.Button(root, text="Изменить размер", command=self.resize_image)
        self.resize_button.grid(row=1, column=0, padx=10, pady=10)

        # Блок информации
        self.info_label = tk.Label(root, text="Информация об изображении:")
        self.info_label.grid(row=2, column=0, padx=10, pady=10)

        self.info_text = tk.Text(root, width=40, height=10)
        self.info_text.grid(row=3, column=0, padx=20, pady=20)

        # Область для отображения изображения
        self.image_label = tk.Label(root)
        self.image_label.grid(row=0, column=1, rowspan=4)

        self.image = None

    def load_image(self):
        start_time = time.time()
        # стадии загрузки изображения
        self.image_path = "path_to_your_image.jpg"  # Замените на ваш путь
        self.image = Image.open(self.image_path)
        self.display_image(self.image)
        self.update_info(self.image_path, self.image.size)
        end_time = time.time()
        memory_used = memory_usage(-1, interval=0.1, timeout=1)
        print(f"Время загрузки: {end_time - start_time:.4f} segundos")
        print(f"Использование памяти после загрузки: {max(memory_used)} MiB")

    def resize_image(self):
        start_time = time.time()
        if self.image:
            self.image = self.image.resize((200, 200))  # Измените на желаемый размер
            self.display_image(self.image)
            self.update_info(self.image_path, self.image.size)
        end_time = time.time()
        memory_used = memory_usage(-1, interval=0.1, timeout=1)
        print(f"Время изменения размера: {end_time - start_time:.4f} секунд")
        print(f"Использование памяти после изменения размера: {max(memory_used)} MiB")

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


if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop()
