import tkinter as tk


def printSelection():
    num = int_gender.get()
    if num == 1:
        lab_print.config(text="你是男生")
    else:
        lab_print.config(text="你是女生")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_1")

    int_gender = tk.IntVar()
    int_gender.set(0) # default value 0, not selected
    lab_print = tk.Label(root, text="这是预设, 尚未选择",
                        bg="lightyellow", width=30)
    lab_print.pack()
    radiobtn_man = tk.Radiobutton(root, text="男生", variable=int_gender,
                                value=1, command=printSelection)
    radiobtn_man.pack()
    radiobtn_woman = tk.Radiobutton(root, text="女生", variable=int_gender,
                                value=2, command=printSelection)
    radiobtn_woman.pack()

    root.mainloop()