import tkinter as tk


def run_counter(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)
    
    counting()


if __name__ == '__main__':
    """ Rewrite program ch2_23.py and add end button.
    Click end button and the program is over."""
    root = tk.Tk()
    root.title("ch4_4")

    digit = tk.Label(root, bg="yellow", fg="blue", height=3,
                    width=10, font="Helvetic 20 bold")
    digit.pack()
    counter = 0
    run_counter(digit)
    tk.Button(root, text="结束", width=15, command=root.destroy).pack(pady=10)

    root.mainloop()