import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_16")
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")
    """
    The first label is placed from the left, and the other two labels
    are configured from top to bottom using the default.
    """
    label1.pack(side=tk.LEFT)
    label2.pack()
    label3.pack()

    window.mainloop()