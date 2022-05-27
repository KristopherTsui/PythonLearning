import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_31")

    label1 = tk.Label(window, text="明志工专")
    label2 = tk.Label(window, bg="yellow", width=20)
    label3 = tk.Label(window, text="明志科技大学")
    label4 = tk.Label(window, bg="aqua", width=20)

    label1.grid(row=0, column=0, padx=5, pady=5)
    label2.grid(row=0, column=1, padx=5, pady=5)
    label3.grid(row=1, column=0, padx=5)
    label4.grid(row=1, column=1, padx=5)

    window.mainloop()