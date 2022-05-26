import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_10")
    # execute multi-line output, and set the last line to be left-aligned output
    label = tk.Label(root, text="abcdefghijklmnopqrstuvwy", fg="blue",
                    bg="lightyellow", wraplength=80, justify="left")
    label.pack()

    root.mainloop()