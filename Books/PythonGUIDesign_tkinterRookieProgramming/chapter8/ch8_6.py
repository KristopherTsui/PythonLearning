from tkinter import Tk
import tkinter.ttk as ttk


if __name__ == '__main__':
    root = Tk()
    root.title("ch8_6")

    style = ttk.Style()
    style.theme_use("alt")

    fm1 = ttk.Frame(root, width=150, height=80, relief="flat")
    fm1.grid(row=0, column=0, padx=5, pady=5)
    fm2 = ttk.Frame(root, width=150, height=80, relief="groove")
    fm2.grid(row=0, column=1, padx=5, pady=5)
    fm3 = ttk.Frame(root, width=150, height=80, relief="raised")
    fm3.grid(row=0, column=2, padx=5, pady=5)
    fm4 = ttk.Frame(root, width=150, height=80, relief="ridge")
    fm4.grid(row=1, column=0, padx=5, pady=5)
    fm5 = ttk.Frame(root, width=150, height=80, relief="solid")
    fm5.grid(row=1, column=1, padx=5, pady=5)
    fm6 = ttk.Frame(root, width=150, height=80, relief="sunken")
    fm6.grid(row=1, column=2, padx=5, pady=5)

    root.mainloop()