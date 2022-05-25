import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    screen_width = root.winfo_screenwidth() # get screen width
    screen_height = root.winfo_screenheight() # get screen height
    width, height = 300, 160
    x = (screen_width - width) / 2
    y = (screen_height - height) / 2
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    # root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.mainloop()