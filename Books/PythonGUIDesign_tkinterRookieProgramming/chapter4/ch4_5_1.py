import tkinter as tk


def bgColor(bg_color):
    root.config(bg=bg_color)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_5_1")
    root.geometry("300x200")

    btn_exit = tk.Button(root, text="Exit", command=root.destroy)
    # use lambda expression
    btn_blue = tk.Button(root, text="Blue", command=lambda:bgColor("blue"))
    btn_yellow = tk.Button(root, text="Yellow", command=lambda:bgColor("yellow"))
    btn_exit.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
    btn_blue.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
    btn_yellow.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()