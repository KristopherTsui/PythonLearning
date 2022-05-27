import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_4")
    # The label background is light yellow and the width is 15.
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow", width=15)
    # The label background is light green and the width is 15.
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen", width=15)
    # The label background is light blue and the width is 15.
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue", width=15)
    label1.pack() # packaging and positioning components
    label2.pack(side=tk.RIGHT) # packaging and positioning components on the right
    label3.pack(side=tk.LEFT) # packaging and positioning components on the left

    window.mainloop()