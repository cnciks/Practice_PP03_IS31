from PIL import Image
from tkinter import messagebox

def resize_and_concatenate(path1, path2, width, height):
    try:
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
