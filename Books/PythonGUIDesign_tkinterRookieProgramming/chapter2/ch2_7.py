import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_7")
    """
    make the text in the label automatically wrap 
    when it reaches a width of 40 pixels
    """
    label = tk.Label(root, text="I like tkinter", fg="blue", bg="yellow",
                    height=3, width=15, anchor=tk.NW, wraplength=40)
    label.pack()

    root.mainloop()