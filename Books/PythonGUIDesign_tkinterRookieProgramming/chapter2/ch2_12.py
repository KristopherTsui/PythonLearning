import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_12")
    # get right output
    label = tk.Label(root, text="abcdefghijklmnopqrstuvwy", fg="blue",
                    bg="lightyellow", wraplength=80, justify="right")
    label.pack()

    root.mainloop()