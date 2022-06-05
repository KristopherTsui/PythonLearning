import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch8_4")

    fm1 = tk.Frame(width=150, height=80, relief=tk.GROOVE, borderwidth=5)
    fm1.pack(side=tk.LEFT, padx=5, pady=5)
    fm2 = tk.Frame(width=150, height=80, relief=tk.RAISED, borderwidth=5)
    fm2.pack(side=tk.LEFT, padx=5, pady=5)
    fm3 = tk.Frame(width=150, height=80, relief=tk.RIDGE, borderwidth=5)
    fm3.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()