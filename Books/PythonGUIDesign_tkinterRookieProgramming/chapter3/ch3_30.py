import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_30")
    tk.Label(window, text="标签1",
            relief="raised").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(window, text="标签2",
            relief="raised").grid(row=0, column=1, padx=5, pady=5)
    tk.Label(window, text="标签3",
            relief="raised").grid(row=0, column=2, padx=5, pady=5)
    tk.Label(window, text="标签4",
            relief="raised").grid(row=0, column=3, padx=5, pady=5)
    tk.Label(window, text="标签5", relief="raised").grid(row=1, column=0, padx=5)
    tk.Label(window, text="标签6", relief="raised").grid(row=1, column=1, padx=5)
    tk.Label(window, text="标签7", relief="raised").grid(row=1, column=2, padx=5)
    tk.Label(window, text="标签8", relief="raised").grid(row=1, column=3, padx=5)
    window.mainloop()