import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_24")

    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow", width=15)
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen", width=15)
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue", width=15)

    # lattice packaging
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    label3.grid(row=1, column=1)

    window.mainloop()