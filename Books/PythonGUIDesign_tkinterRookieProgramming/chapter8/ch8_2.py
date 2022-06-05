import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch8_2")

    fms = {'red': 'cross', 'green': 'boat', 'blue': 'clock'}
    for fmColor in fms:
        tk.Frame(root, bg=fmColor, cursor=fms[fmColor],
                height=50, width=250).pack(side=tk.LEFT)

    root.mainloop()