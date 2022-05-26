import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_2")
    label = tk.Label(root, text="I like tkinter").pack()
    print(type(label)) # return the label data type
    
    root.mainloop()