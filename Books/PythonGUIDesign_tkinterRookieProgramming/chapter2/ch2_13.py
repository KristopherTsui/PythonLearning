import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_13")
    # display hourglass bitmap at label position
    label = tk.Label(root, bitmap="hourglass")
    label.pack()

    root.mainloop()