import tkinter as tk


def callbackW(*args):
    str_lab.set(str_entry.get())


def callbackR(*args):
    print("Warning: 数据被读取!")


def read():
    print("读取数据:", str_entry.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch6_5")

    str_entry = tk.StringVar()
    entry_input = tk.Entry(root, textvariable=str_entry)
    entry_input.pack(pady=5, padx=10)
    str_entry.trace("w", callbackW)
    str_entry.trace("r", callbackR)

    str_lab = tk.StringVar()
    lab = tk.Label(root, textvariable=str_lab)
    str_lab.set("同步显示")
    lab.pack(pady=5, padx=10)

    btn_read = tk.Button(root, text="读取", command=read)
    btn_read.pack(pady=5)

    root.mainloop()