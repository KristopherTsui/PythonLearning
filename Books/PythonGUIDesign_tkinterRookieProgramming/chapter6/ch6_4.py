import tkinter as tk


def callback(*args):
    str_label.set(str_entry.get())
    print("data changed:", str_entry.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch6_4")

    str_entry = tk.StringVar()
    entry_trace = tk.Entry(root, textvariable=str_entry)
    entry_trace.pack(pady=5, padx=10)
    str_entry.trace("w", callback)

    str_label = tk.StringVar()
    lab = tk.Label(root, textvariable=str_label)
    str_label.set("同步显示")
    lab.pack(pady=5, padx=10)

    root.mainloop()