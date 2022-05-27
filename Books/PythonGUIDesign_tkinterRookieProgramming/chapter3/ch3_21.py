import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_21")
    root.geometry("300x200")
    # Configure labels from top to bottom, 
    # and experience the application of expand parameter and fill parameter.
    tk.Label(root, text="Mississippi", bg="red", fg="white",
            font="Times 24 bold").pack(fill=tk.X)
    tk.Label(root, text="Kentucky", bg="green", fg="white",
            font="Arial 24 bold italic").pack(fill=tk.BOTH, expand=True)
    tk.Label(root, text="Purdue", bg="blue", fg="white",
            font="Times 24 bold").pack(fill=tk.X)

    root.mainloop()