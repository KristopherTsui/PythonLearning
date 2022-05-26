import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_25")
    label = tk.Label(root, text="I like tkinter")
    label.pack()
    print(label.keys()) # return all parameters of the label object

    root.mainloop()