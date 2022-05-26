import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_17")
    # create a tag for the raised attribute
    # use the relief property to establish the border of the Widget control
    label = tk.Label(root, text="raised", relief="raised")
    label.pack()

    root.mainloop()