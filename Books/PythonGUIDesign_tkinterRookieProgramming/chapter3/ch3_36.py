import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_36")

    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow", width=15)
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen", width=15)
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue", width=15)

    # use the place() method to directly set the position of label
    label1.place(x=0, y=0)
    label2.place(x=30, y=50)
    label3.place(x=60, y=100)

    window.mainloop()