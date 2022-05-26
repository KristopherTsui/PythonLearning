import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_8_1")
    # use Helvetic glyphs, size 20, bold
    label = tk.Label(root, text="I like tkinter", fg="blue", bg="yellow",
                    height=3, width=15, font=("Helvetic", 20, "bold"))
    label.pack()

    root.mainloop()