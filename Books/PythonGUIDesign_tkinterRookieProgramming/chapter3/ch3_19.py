import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_19")
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")
    label1.pack(side=tk.LEFT, fill=tk.Y)
    label2.pack(fill=tk.X)
    # configure from top to bottom by the default and use fill=tk.BOTH
    # but it has no effect and we need use expand parameter
    label3.pack(fill=tk.BOTH)

    window.mainloop()