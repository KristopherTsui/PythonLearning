import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch5_2")
    lab_account = tk.Label(root, text="Account")
    lab_pwd = tk.Label(root, text="Password")
    entry_account = tk.Entry(root)
    ## The characters entered when entering the password will be hidden
    ## and displayed with * characters.
    entry_pwd = tk.Entry(root, show='*')
    lab_account.grid(row=0)
    lab_pwd.grid(row=1)
    entry_account.grid(row=0, column=1)
    entry_pwd.grid(row=1, column=1)

    root.mainloop()