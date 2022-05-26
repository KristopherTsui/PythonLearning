import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_6")
    # make string output at the bottom right of the label
    label = tk.Label(root, text="I like tkinter", fg="blue",
                    bg="yellow", height=3, width=15, anchor="se")
    label.pack()

    root.mainloop()