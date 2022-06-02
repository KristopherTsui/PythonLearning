import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch5_1")
    ## set label and entry in window, input name and address.
    lab_name = tk.Label(root, text="Name")
    lab_address = tk.Label(root, text="Address")
    entry_name = tk.Entry(root)
    entry_address = tk.Entry(root)

    lab_name.grid(row=0)
    lab_address.grid(row=1)
    entry_name.grid(row=0, column=1)
    entry_address.grid(row=1, column=1)

    root.mainloop()