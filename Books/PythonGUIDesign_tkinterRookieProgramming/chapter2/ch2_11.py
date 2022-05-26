import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_11")
    # get forced centered output
    label = tk.Label(root, text="abcdefghijklmnopqrstuvwy", fg="blue",
                    bg="lightyellow", wraplength=80, justify="center")
    label.pack()

    root.mainloop()