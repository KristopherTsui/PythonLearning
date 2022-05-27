import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_2")
    # The label background is light yellow and the label width is 15.
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow", width=15)
    # The label background is light green and the label width is 15.
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen", width=15)
    # The label background is light blue and the label width is 15.
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue", width=15)
    # packaging and positioning components
    label1.pack(side=tk.BOTTOM)
    label2.pack(side=tk.BOTTOM)
    label3.pack(side=tk.BOTTOM)

    window.mainloop()