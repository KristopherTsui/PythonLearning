import tkinter as tk


def callbackW(name, index, mode):
    str_lab.set(str_entry.get())
    print(f"name = {name}, index = {index}, mode = {mode}")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch6_6")

    str_entry = tk.StringVar()
    entry_input = tk.Entry(root, textvariable=str_entry)
    entry_input.pack(pady=5, padx=10)
    str_entry.trace("w", callbackW)

    str_lab = tk.StringVar()
    lab = tk.Label(root, textvariable=str_lab)
    str_lab.set("同步显示")
    lab.pack(pady=5, padx=10)

    root.mainloop()