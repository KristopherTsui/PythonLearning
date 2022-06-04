import tkinter as tk


def printSelection():
    lab_print.config(text="你是"+str_gender.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_2")

    str_gender = tk.StringVar()
    str_gender.set("男生")
    lab_print = tk.Label(root, text="这是默认值, 默认男生",
                        bg="lightyellow", width=30)
    lab_print.pack()
    radiobtn_man = tk.Radiobutton(root, text="男生", variable=str_gender,
                                value="男生", command=printSelection)
    radiobtn_man.pack()
    radiobtn_woman = tk.Radiobutton(root, text="女生", variable=str_gender,
                                value="女生", command=printSelection)
    radiobtn_woman.pack()

    root.mainloop()