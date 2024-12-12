import tkinter as tk
import time
from image_handler import ImageHandler
from ui import create_ui

def main():
    start_time = time.time()  # Сохраняем начало выполнения

    root = tk.Tk()
    root.title("Склеивание изображений")

    # Замеряем время создания экземпляра ImageHandler
    image_handler_start_time = time.time()
    image_handler = ImageHandler()
    image_handler_duration = time.time() - image_handler_start_time
    print(f"Время создания ImageHandler: {image_handler_duration:.4f} секунд")

    # Замеряем время создания интерфейса
    create_ui_start_time = time.time()
    create_ui(root, image_handler)
    create_ui_duration = time.time() - create_ui_start_time
    print(f"Время создания интерфейса: {create_ui_duration:.4f} секунд")

    root.mainloop()

    total_duration = time.time() - start_time
    print(f"Общее время выполнения программы: {total_duration:.4f} секунд")

if __name__ == "__main__":
    main()
