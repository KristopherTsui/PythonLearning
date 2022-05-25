import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    width = 300 # window width
    height = 160 # window height
    x = 400 # the x coordinate of the upper left corner of the window
    y = 200 # the y coordinate of the upper left corner of the window
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.mainloop()