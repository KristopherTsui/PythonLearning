import tkinter as tk


def callback(*args):
    print("data changed:", str_x.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch6_3")

    str_x = tk.StringVar()
    entry_trace = tk.Entry(root, textvariable=str_x)
    entry_trace.pack(pady=5, padx=10)
    str_x.trace("w", callback) # if there is a change, execute callback

    root.mainloop()