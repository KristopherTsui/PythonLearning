import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_26")
    tk.Label(window, text="标签1", relief="raised").grid(row=0, column=0)
    tk.Label(window, text="标签2", relief="raised").grid(row=0, column=1)
    tk.Label(window, text="标签3", relief="raised").grid(row=0, column=2)
    tk.Label(window, text="标签4", relief="raised").grid(row=0, column=3)
    tk.Label(window, text="标签5", relief="raised").grid(row=1, column=0)
    tk.Label(window, text="标签6", relief="raised").grid(row=1, column=1)
    tk.Label(window, text="标签7", relief="raised").grid(row=1, column=2)
    tk.Label(window, text="标签8", relief="raised").grid(row=1, column=3)

    window.mainloop()