import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_18")
    """
    make the background of the label light yellow, 
    set the left and right spacing between the label text and the label interval to 5,
    and set the upper and lower spacing between the label text and the interval to 10.
    """
    label = tk.Label(root, text="raised", relief="raised",
                    bg="lightyellow", padx=5, pady=10)
    label.pack()

    root.mainloop()