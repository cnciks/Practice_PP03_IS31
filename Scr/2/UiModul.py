import tkinter as tk
from tkinter import messagebox

def create_ui(root, image_handler):
    frame_left = tk.Frame(root)
    frame_left.pack(side=tk.LEFT, padx=10, pady=10)

    frame_right = tk.Frame(root)
    frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

    tk.Label(frame_left, text="Первое изображение:").pack(anchor='w')
    entry_image1 = tk.Entry(frame_left, width=50)
    entry_image1.pack()
    tk.Button(frame_left, text="Загрузить", 
              command=lambda: load_image(1, entry_image1, image_handler)).pack()

    tk.Label(frame_left, text="Второе изображение:").pack(anchor='w')
    entry_image2 = tk.Entry(frame_left, width=50)
    entry_image2.pack()
    tk.Button(frame_left, text="Загрузить", 
              command=lambda: load_image(2, entry_image2, image_handler)).pack()

    tk.Button(frame_left, text="Склеить изображения", 
              command=lambda: resize_and_concatenate(image_handler)).pack(pady=10)

    tk.Label(frame_left, text="Ширина:").pack(anchor='w')
    entry_width = tk.Entry(frame_left)
    entry_width.pack()
    entry_width.insert(0, "300")  # Значение по умолчанию

    tk.Label(frame_left, text="Высота:").pack(anchor='w')
    entry_height = tk.Entry(frame_left)
    entry_height.pack()
    entry_height.insert(0, "300")  # Значение по умолчанию

    label_concatenated_image = tk.Label(frame_right)
    label_concatenated_image.pack()

    def load_image(image_number, entry_widget, image_handler):
        path = image_handler.load_image(image_number)
        if path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, path)

    def resize_and_concatenate(image_handler):
        width = int(entry_width.get())
        height = int(entry_height.get())
        output_path, result_img = image_handler.resize_and_concatenate(width, height)
        if output_path:
            messagebox.showinfo("Успех", f"Изображения успешно склеены и сохранены по адресу: {output_path}")
            display_concatenated_image(result_img, label_concatenated_image)

    def display_concatenated_image(result_img, label_widget):
        img_display = ImageTk.PhotoImage(result_img)
        label_widget.config(image=img_display)
        label_widget.image = img_display
