import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_11")

    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")
    label1.pack()
    # set the x-axis spacing between the label text and the text container to 10
    label2.pack(ipadx=10)
    # set the y-axis spacing between the label text and the text container to 10
    label3.pack(ipady=10)

    window.mainloop()