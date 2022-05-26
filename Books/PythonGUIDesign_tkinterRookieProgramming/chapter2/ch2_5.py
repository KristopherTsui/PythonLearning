import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_5")
    # make the string output from the upper left corner of the label interval
    label = tk.Label(root, text="I like tkinter", fg="blue",
                    bg="yellow", height=3, width=15, anchor="nw")
    label.pack()

    root.mainloop()