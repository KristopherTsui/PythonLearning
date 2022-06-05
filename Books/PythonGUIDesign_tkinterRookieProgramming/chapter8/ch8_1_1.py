import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch8_1_1")

    for fm in ["red", "green", "blue"]:
        ## ignore father object when calling tk.Frame
        tk.Frame(bg=fm, height=50, width=250).pack()

    root.mainloop()