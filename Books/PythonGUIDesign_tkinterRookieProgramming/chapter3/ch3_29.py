import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_29")

    label1 = tk.Label(window, text="标签1", relief="raised")
    label2 = tk.Label(window, text="标签2", relief="raised")
    label4 = tk.Label(window, text="标签4", relief="raised")
    label5 = tk.Label(window, text="标签5", relief="raised")
    label8 = tk.Label(window, text="标签8", relief="raised")
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1, rowspan=2, columnspan=2)
    label4.grid(row=0, column=3)
    label5.grid(row=1, column=0)
    label8.grid(row=1, column=3)
    window.mainloop()