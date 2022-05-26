import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_4")
    """
    set the label width to 15, height to 3, background color to yellow
    and foreground color to blue
    """
    label = tk.Label(root, text="I like tkinter", fg="blue",
                    bg="yellow", height=3, width=15)
    label.pack()

    root.mainloop()