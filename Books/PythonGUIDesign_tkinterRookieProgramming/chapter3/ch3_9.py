import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_9")

    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow", width=15)
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen", width=15)
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue", width=15)
    label1.pack(side=tk.LEFT)
    label2.pack(side=tk.LEFT, padx=10) # left and right spacing padx=10
    label3.pack(side=tk.LEFT)

    window.mainloop()