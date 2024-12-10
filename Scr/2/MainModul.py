import tkinter as tk
from image_loader import load_image
from image_processor import resize_and_concatenate

# Создание главного окна
root = tk.Tk()
root.title("Склеивание изображений")

# Поля ввода для путей к изображениям
tk.Label(root, text="Первое изображение:").pack()
entry_image1 = tk.Entry(root, width=50)
entry_image1.pack()
tk.Button(root, text="Загрузить", command=lambda: load_image(entry_image1)).pack()

tk.Label(root, text="Второе изображение:").pack()
entry_image2 = tk.Entry(root, width=50)
entry_image2.pack()
tk.Button(root, text="Загрузить", command=lambda: load_image(entry_image2)).pack()

# Поля ввода для размеров изображений
tk.Label(root, text="Ширина:").pack()
entry_width = tk.Entry(root)
entry_width.pack()
entry_width.insert(0, "300")  # Значение по умолчанию

tk.Label(root, text="Высота:").pack()
entry_height = tk.Entry(root)
entry_height.pack()
entry_height.insert(0, "300")  # Значение по умолчанию

# Кнопка для выполнения склеивания
tk.Button(root, text="Склеить изображения", command=lambda: resize_and_concatenate(entry_image1.get(), entry_image2.get(), int(entry_width.get()), int(entry_height.get()))).pack()

# Запуск главного цикла
root.mainloop()
