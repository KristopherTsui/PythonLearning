import tkinter as tk
from PIL import Image, ImageTk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_19_1")
    root.geometry("680x400")

    image = Image.open("../imgs/wallpaper.jpg")
    wallpaper = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=wallpaper)
    label.pack()

    root.mainloop()