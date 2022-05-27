import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_1")
    # The label background is light yellow.
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    # The label background is light green.
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    # The label background is light blue.
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")
    # packaging and positioning components
    label1.pack()
    label2.pack()
    label3.pack()

    window.mainloop()