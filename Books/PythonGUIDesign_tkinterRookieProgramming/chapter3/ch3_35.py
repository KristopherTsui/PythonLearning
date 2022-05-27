import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_35")

    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

    r = 0 # row number
    for color in color_list:
        tk.Label(root, text=color, relief="groove", width=20).grid(row=r, column=0)
        tk.Label(root, bg=color, relief="ridge", width=20).grid(row=r, column=1)
        r += 1

    root.mainloop()