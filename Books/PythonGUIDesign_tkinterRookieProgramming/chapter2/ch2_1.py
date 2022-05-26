import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_1")
    # the first parameter is the parent object
    label = tk.Label(root, text="I like tkinter")
    label.pack() # packaging and positioning components
    print(type(label)) # return the label data type

    root.mainloop()