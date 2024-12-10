import tkinter as tk
from image_handler import ImageHandler
from ui import create_ui

def main():
    root = tk.Tk()
    root.title("Склеивание изображений")

    image_handler = ImageHandler()
    create_ui(root, image_handler)

    root.mainloop()

if __name__ == "__main__":
    main()
