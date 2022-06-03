import tkinter as tk


def hit():
    ## use get method replace bool variable
    if str_x.get() == "":
        str_x.set("I like tkinter")
    else:
        str_x.set("")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch6_2")

    str_x = tk.StringVar()
    lab = tk.Label(root, textvariable=str_x, fg="blue", bg="lightyellow",
                    font="Verdana 16 bold", width=25, height=2)
    lab.pack()
    btn_hit = tk.Button(root, text="Click Me", command=hit)
    btn_hit.pack()

    root.mainloop()