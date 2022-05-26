import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_24")
    label = tk.Label(root, text="raised", relief="raised", bg="lightyellow",       
                    padx=5, pady=10, cursor="heart") # cursor shape
    label.pack()

    root.mainloop()