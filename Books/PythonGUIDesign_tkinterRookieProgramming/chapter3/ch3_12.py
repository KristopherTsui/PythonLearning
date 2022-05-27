import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_12")
    root.geometry("300x180")

    label_ok = tk.Label(root, text="OK", font="Times 20 bold",
                        fg="white", bg="blue")
    # set in the sourth direction from the right
    # the spacing of x-axis and y-axis are 10
    label_ok.pack(anchor=tk.S, side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()