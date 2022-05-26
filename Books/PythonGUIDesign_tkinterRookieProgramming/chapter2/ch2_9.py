import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_9")
    """
    use the default way to perform multi-line output,
    and observe that the last line is center-aligned output
    """
    label = tk.Label(root, text="abcdefghijklmnopqrstuvwy", fg="blue",
                    bg="lightyellow", wraplength=80)
    label.pack()

    root.mainloop()