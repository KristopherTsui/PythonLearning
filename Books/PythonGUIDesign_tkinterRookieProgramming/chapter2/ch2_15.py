import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_15")
    # When the image and the text coexist, the image is on top.
    label = tk.Label(root, bitmap="hourglass", compound="top", text="我的天空")
    label.pack()

    root.mainloop()