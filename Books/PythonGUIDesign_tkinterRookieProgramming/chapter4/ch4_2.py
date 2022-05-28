import tkinter as tk


def message_show():
    # use config() method to replace three other sentences
    label.config(text="I love Python", bg="lightyellow", fg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_2")
    
    label = tk.Label(root)
    btn = tk.Button(root, text="打印消息", command=message_show)
    label.pack()
    btn.pack()

    root.mainloop()