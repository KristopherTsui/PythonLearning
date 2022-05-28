import tkinter as tk


def message_show():
    label.config(text="I love Pyhton", bg="lightyellow", fg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_3")
    
    label = tk.Label(root)
    btn1 = tk.Button(root, text="打印消息", width=15, command=message_show)
    # If click end button, the window can be closed.
    btn2 = tk.Button(root, text="结束", width=15, command=root.destroy)
    label.pack()
    btn1.pack(side=tk.LEFT)
    btn2.pack(side=tk.LEFT)

    root.mainloop()