import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_8")
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow", width=15)
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen", width=15)
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue", width=15)
    # left and right border spacing is 50 pixels
    label1.pack(padx=50)
    label2.pack(padx=50)
    label3.pack(padx=50)

    window.mainloop()