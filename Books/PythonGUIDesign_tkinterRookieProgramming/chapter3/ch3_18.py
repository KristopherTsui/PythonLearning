import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_18")
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")
    """
    The first label is configured from the left while using `fill=tk.Y`, and the
    other two labels are configured from top to bottom while using `fill=tk.X`.
    """
    label1.pack(side=tk.LEFT, fill=tk.Y)
    label2.pack(fill=tk.X)
    label3.pack(fill=tk.X)

    window.mainloop()