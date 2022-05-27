import tkinter as tk


if __name__ == '__main__':
    Reliefs = ["flat", "groove", "raised", "ridge", "solid", "sunken"]

    root = tk.Tk()
    root.title("ch3_5")

    # list all attributes of relief
    for Relief in Reliefs:
        tk.Label(root, text=Relief, relief=Relief, fg="blue",
                font="Times 20 bold").pack(side=tk.LEFT, padx=5)
    
    root.mainloop()