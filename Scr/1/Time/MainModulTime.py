import time
import sys
from tkinter import Tk
from app import ImageUtilityApp

# Функция для измерения времени выполнения
def time_func(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Время выполнения '{func.__name__}': {end_time - start_time:.6f} секунд")
    return result

# Функция для измерения размера объекта
def print_size(obj, obj_name="Объект"):
    print(f"Размер {obj_name}: {sys.getsizeof(obj)} байт")

if __name__ == "__main__":
    root = Tk()

    # Измеряем размер окна
    print_size(root, "root")

    # Создаем приложение и измеряем время выполнения
    app = time_func(ImageUtilityApp, root)

    # Измеряем размер приложения
    print_size(app, "app")

    root.mainloop()
