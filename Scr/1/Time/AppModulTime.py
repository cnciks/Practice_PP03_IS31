import time
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from ui import UI
from image_processor import ImageProcessor

class ImageUtilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Утилита работы с изображениями, практикант: Шевель Милена Александровна")

        # Инициализация пользовательского интерфейса
        self.ui = UI(root)
        self.image_processor = ImageProcessor()

        # Связывание кнопок с действиями
        self.ui.load_button.config(command=self.load_image)
        self.ui.resize_button.config(command=self.resize_image)

    def load_image(self):
        start_time = time.perf_counter()  # Начало измерения времени
        self.image_processor.load_image(filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")]))
        load_time = time.perf_counter() - start_time  # Конец измерения времени

        if not self.image_processor.image_path:
            return

        self.ui.display_image(self.image_processor.image)
        self.ui.update_info(self.image_processor.image_path, self.image_processor.image.size)

        # Вывод времени загрузки изображения и его размеров
        print(f"Время загрузки изображения: {load_time:.4f} секунд")
        print(f"Размер загруженного изображения: {sys.getsizeof(self.image_processor.image)} байт")

    def resize_image(self):
        if self.image_processor.image is None:
            messagebox.showwarning("Warning", "Сначала загрузите изображение")
            return

        new_width = simpledialog.askinteger("Изменить размер", "Новая ширина:")
        new_height = simpledialog.askinteger("Изменить размер", "Новая высота:")

        if new_width is not None and new_height is not None:
            start_time = time.perf_counter()  # Начало измерения времени
            resized_image = self.image_processor.resize_image(new_width, new_height)
            resize_time = time.perf_counter() - start_time  # Конец измерения времени

            self.ui.display_image(resized_image)

            # Вывод времени изменения размера изображения и его новых размеров
            print(f"Время изменения размера изображения: {resize_time:.4f} секунд")
            print(f"Размер измененного изображения: {sys.getsizeof(resized_image)} байт")
