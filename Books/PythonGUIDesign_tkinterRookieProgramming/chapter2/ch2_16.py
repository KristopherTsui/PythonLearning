import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_16")
    # Image overlaid on top of image when coexisting with text.
    label = tk.Label(root, bitmap="hourglass", compound="center", text="我的天空")
    label.pack()

    root.mainloop()