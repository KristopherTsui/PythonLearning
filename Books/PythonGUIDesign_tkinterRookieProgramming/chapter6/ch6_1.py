import tkinter as tk


def hit():
    global msg_on
    if msg_on == False:
        msg_on = True
        str_x.set("I like tkinter")
    else:
        msg_on = False
        str_x.set("")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch6_1")

    msg_on = False
    str_x = tk.StringVar()
    lab = tk.Label(root, textvariable=str_x, fg="blue", bg="lightyellow",
                    font="Verdana 16 bold", width=25, height=2)
    lab.pack()
    btn_hit = tk.Button(root, text="Click Me", command=hit)
    btn_hit.pack()

    root.mainloop()