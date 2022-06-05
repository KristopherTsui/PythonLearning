import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch8_5")

    fm = tk.Frame(width=150, height=80, relief=tk.RAISED, borderwidth=5)
    lab = tk.Label(fm, text="Please select program laguages you usually use")
    lab.pack()
    cbPython = tk.Checkbutton(fm, text="Python")
    cbPython.pack(anchor=tk.W)
    cbJava = tk.Checkbutton(fm, text="Java")
    cbJava.pack(anchor=tk.W)
    cbRuby = tk.Checkbutton(fm, text="Ruby")
    cbRuby.pack(anchor=tk.W)
    fm.pack(padx=10, pady=10)

    root.mainloop()