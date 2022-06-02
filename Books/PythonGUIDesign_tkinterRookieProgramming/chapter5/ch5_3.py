import tkinter as tk


if __name__ == '__main__':
    ## create a company web login interface
    root = tk.Tk()
    root.title("ch5_3")
    msg = "欢迎进入 You Tube 系统"
    gif_youtube = tk.PhotoImage(file="../imgs/youtube.gif")
    lab_logo = tk.Label(root, image=gif_youtube, text=msg, compound=tk.BOTTOM)
    lab_account = tk.Label(root, text="Account")
    lab_pwd = tk.Label(root, text="Password")
    entry_account = tk.Entry(root)
    entry_pwd = tk.Entry(root, show="*")
    lab_logo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lab_account.grid(row=1)
    lab_pwd.grid(row=2)
    entry_account.grid(row=1, column=1)
    entry_pwd.grid(row=2, column=1, pady=10)
    root.mainloop()