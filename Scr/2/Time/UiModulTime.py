import time
from memory_profiler import memory_usage
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk  # Не забудьте импортировать Image из PIL, возможно, это нужно для вашей работы.
# Предполагается, что ваши методы load_image и resize_and_concatenate правильно реализованы.

def create_ui(root, image_handler):
    ...

    def load_image(image_number, entry_widget, image_handler):
        start_time = time.time()
        mem_usage = memory_usage((image_handler.load_image, (image_number,)), max_usage=True)
        path = image_handler.load_image(image_number)
        end_time = time.time()

        messagebox.showinfo("Загрузка изображения", f"Время загрузки: {end_time - start_time:.4f} секунд\\nИспользование памяти: {mem_usage[0]} МБ")

        if path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, path)

    def resize_and_concatenate(image_handler):
        width = int(entry_width.get())
        height = int(entry_height.get())

        start_time = time.time()
        mem_usage = memory_usage((image_handler.resize_and_concatenate, (width, height)), max_usage=True)
        output_path, result_img = image_handler.resize_and_concatenate(width, height)
        end_time = time.time()

        messagebox.showinfo("Объединение изображений", f"Время склеивания: {end_time - start_time:.4f} секунд\\nИспользование памяти: {mem_usage[0]} МБ")

        if output_path:
            messagebox.showinfo("Успех", f"Изображения успешно склеены и сохранены по адресу: {output_path}")
            display_concatenated_image(result_img, label_concatenated_image)
