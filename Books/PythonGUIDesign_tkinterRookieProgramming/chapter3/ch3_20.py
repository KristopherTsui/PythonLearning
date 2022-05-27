import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_20")

    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")

    label1.pack(side=tk.LEFT, fill=tk.Y)
    label2.pack(fill=tk.X)
    label3.pack(fill=tk.BOTH, expand=True) # use parameter expand=True

    window.mainloop()