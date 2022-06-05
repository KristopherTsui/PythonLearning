import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch8_1")
    
    for fm in ["red", "green", "blue"]:
        ## set three frames with different background colors
        tk.Frame(root, bg=fm, height=50, width=250).pack()

    root.mainloop()