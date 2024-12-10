import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def load_image1():
    path = filedialog.askopenfilename(title="Выберите первое изображение", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if path:
        entry_image1.delete(0, tk.END)
        entry_image1.insert(0, path)

def load_image2():
    path = filedialog.askopenfilename(title="Выберите второе изображение", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if path:
        entry_image2.delete(0, tk.END)
        entry_image2.insert(0, path)

def resize_and_concatenate():
    try:
        path1 = entry_image1.get()
        path2 = entry_image2.get()
        width = int(entry_width.get())
        height = int(entry_height.get())

        # Открываем изображения и изменяем их размеры
        img1 = Image.open(path1).resize((width, height))
        img2 = Image.open(path2).resize((width, height))

        # Склеиваем изображения
        result_img = Image.new('RGB', (width * 2, height))
        result_img.paste(img1, (0, 0))
        result_img.paste(img2, (width, 0))

        # Сохраняем результат
        output_path = path1.rsplit('/', 1)[0] + '/concatenated_image.jpg'
        result_img.save(output_path)

        messagebox.showinfo("Успех", f"Изображения успешно склеены и сохранены по адресу: {output_path}")

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Создание главного окна
root = tk.Tk()
root.title("Склеивание изображений")

# Поля ввода для путей к изображениям
tk.Label(root, text="Первое изображение:").pack()
entry_image1 = tk.Entry(root, width=50)
entry_image1.pack()
tk.Button(root, text="Загрузить", command=load_image1).pack()

tk.Label(root, text="Второе изображение:").pack()
entry_image2 = tk.Entry(root, width=50)
entry_image2.pack()
tk.Button(root, text="Загрузить", command=load_image2).pack()

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
tk.Button(root, text="Склеить изображения", command=resize_and_concatenate).pack()

# Запуск главного цикла
root.mainloop()
