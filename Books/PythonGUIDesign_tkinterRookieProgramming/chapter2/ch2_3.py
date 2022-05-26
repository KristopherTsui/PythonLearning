import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_3")
    # set the text foreground color is blue and background color is yellow
    label = tk.Label(root, text="I like tkinter", fg="blue", bg="yellow")
    label.pack()

    root.mainloop()