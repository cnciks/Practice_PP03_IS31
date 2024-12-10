import tkinter as tk
from tkinter import filedialog

def load_image(entry):
    path = filedialog.askopenfilename(title="Выберите изображение", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)
