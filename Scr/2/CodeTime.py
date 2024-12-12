import time

# фиксируем время старта работы кода
start = time.time()

# код, время работы которого измеряется
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def load_image1():
    path = filedialog.askopenfilename(title="Выберите первое изображение", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if path:
        entry_image1.delete(0, tk.END)
        entry_image1.insert(0, path)
        update_image_info(1, path)

def load_image2():
    path = filedialog.askopenfilename(title="Выберите второе изображение", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if path:
        entry_image2.delete(0, tk.END)
        entry_image2.insert(0, path)
        update_image_info(2, path)

def update_image_info(image_number, path):
    try:
        img = Image.open(path)
        info = f"Изображение {image_number}: {path}\\nРазмер: {img.size[0]}x{img.size[1]}"
        if image_number == 1:
            label_image_info1.config(text=info)
        elif image_number == 2:
            label_image_info2.config(text=info)
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

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

        # Отображение склеенного изображения
        display_concatenated_image(result_img)

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def display_concatenated_image(result_img):
    # Отображение обработанного изображения
    img_display = ImageTk.PhotoImage(result_img)
    label_concatenated_image.config(image=img_display)
    label_concatenated_image.image = img_display

# Создание главного окна
root = tk.Tk()
root.title("Склеивание изображений")

# Создание фреймов для организации макета
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

# Поля ввода для путей к изображениям
tk.Label(frame_left, text="Первое изображение:").pack(anchor='w')
entry_image1 = tk.Entry(frame_left, width=50)
entry_image1.pack()
tk.Button(frame_left, text="Загрузить", command=load_image1).pack()

tk.Label(frame_left, text="Второе изображение:").pack(anchor='w')
entry_image2 = tk.Entry(frame_left, width=50)
entry_image2.pack()
tk.Button(frame_left, text="Загрузить", command=load_image2).pack()

# Кнопка для выполнения склеивания
tk.Button(frame_left, text="Склеить изображения", command=resize_and_concatenate).pack(pady=10)

# Поля ввода для размеров изображений
tk.Label(frame_left, text="Ширина:").pack(anchor='w')
entry_width = tk.Entry(frame_left)
entry_width.pack()
entry_width.insert(0, "300")  # Значение по умолчанию

tk.Label(frame_left, text="Высота:").pack(anchor='w')
entry_height = tk.Entry(frame_left)
entry_height.pack()
entry_height.insert(0, "300")  # Значение по умолчанию

# Метки для отображения информации об изображениях
label_image_info1 = tk.Label(frame_left, text="")
label_image_info1.pack(anchor='w')

label_image_info2 = tk.Label(frame_left, text="")
label_image_info2.pack(anchor='w')

# Метка для отображения склеенного изображения
label_concatenated_image = tk.Label(frame_right)
label_concatenated_image.pack()

# Запуск главного цикла
root.mainloop()

# фиксируем время окончания работы кода
finish = time.time()

# вычитаем время старта из времени окончания и получаем результат в миллисекундах
res = finish - start
res_msec = res*1000
print("Время работы в миллисекундах:", res_msec)
