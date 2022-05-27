import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_22")
    # configure the labels from left to right,
    # and experience the application of expand parameter and fill paremeter.
    tk.Label(root, text="Mississippi", bg='red', fg="white",
            font="Times 20 bold").pack(side=tk.LEFT, fill=tk.Y)
    tk.Label(root, text="Kentucky", bg="green", font="Arial 20 bold italic",
            fg="white").pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tk.Label(root, text="Purdue", bg="blue", fg="white",
            font="Times 20 bold").pack(side=tk.LEFT, fill=tk.Y)
    
    root.mainloop()