import tkinter as tk


def calculate():
    result = eval(str_equ.get())
    str_equ.set(str_equ.get()+"=\n"+str(result))


def show(str_bnt):
    content = str_equ.get()
    if content == "0":
        content = ""
    str_equ.set(content+str_bnt)


def backspace():
    str_equ.set(str(str_equ.get()[:-1]))


def clear():
    str_equ.set("0")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("计算器")

    ## design display area
    str_equ = tk.StringVar()
    str_equ.set("0")
    lab_display = tk.Label(root, width=25, height=2, relief="raised",
                            anchor=tk.SE, textvariable=str_equ)
    lab_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    ## button for clearing the display area
    btn_clear = tk.Button(root, text="C", fg="blue", width=5, command=clear)
    btn_clear.grid(row=1, column=0)

    ## other buttons in row one
    tk.Button(root, text="DEL", width=5, command=backspace).grid(row=1, column=1)
    tk.Button(root, text="%", width=5,
            command=lambda:show("%")).grid(row=1, column=2)
    tk.Button(root, text="/", width=5,
            command=lambda:show("/")).grid(row=1, column=3)
    ## buttons in row two
    tk.Button(root, text="7", width=5,
            command=lambda:show("7")).grid(row=2, column=0)
    tk.Button(root, text="8", width=5,
            command=lambda:show("8")).grid(row=2, column=1)
    tk.Button(root, text="9", width=5,
            command=lambda:show("9")).grid(row=2, column=2)
    tk.Button(root, text="*", width=5,
            command=lambda:show("*")).grid(row=2, column=3)
    ## buttons for row three
    tk.Button(root, text="4", width=5,
            command=lambda:show("4")).grid(row=3, column=0)
    tk.Button(root, text="5", width=5,
            command=lambda:show("5")).grid(row=3, column=1)
    tk.Button(root, text="6", width=5,
            command=lambda:show("6")).grid(row=3, column=2)
    tk.Button(root, text="-", width=5,
            command=lambda:show("-")).grid(row=3, column=3)
    ## buttons for row four
    tk.Button(root, text="1", width=5,
            command=lambda:show("1")).grid(row=4, column=0)
    tk.Button(root, text="2", width=5,
            command=lambda:show("2")).grid(row=4, column=1)
    tk.Button(root, text="3", width=5,
            command=lambda:show("3")).grid(row=4, column=2)
    tk.Button(root, text="+", width=5,
            command=lambda:show("+")).grid(row=4, column=3)
    ## buttons for row five
    tk.Button(root, text="0", width=12,
            command=lambda:show("0")).grid(row=5, column=0, columnspan=2)
    tk.Button(root, text=".", width=5,
            command=lambda:show(".")).grid(row=5, column=2)
    tk.Button(root, text="=", width=5,
            command=calculate).grid(row=5, column=3)

    root.mainloop()