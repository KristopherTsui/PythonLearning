import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    # create a 300x160 size window
    # the coordinates of the upper left corner of the window are (400,200)
    root.geometry("300x160+400+200")
    root.mainloop()