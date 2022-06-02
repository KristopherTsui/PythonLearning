import tkinter as tk


def printInfo():
    print(f"Account: {entry_account.get()}\nPassword: {entry_pwd.get()}")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch5_4")

    message = "欢迎进入 You Tube 系统"
    gif_tube = tk.PhotoImage(file="../imgs/youtube.gif")
    lab_logo = tk.Label(root, image=gif_tube, text=message, compound=tk.BOTTOM)
    lab_account = tk.Label(root, text="Account")
    lab_pwd = tk.Label(root, text="Password")
    entry_account = tk.Entry(root)
    entry_pwd = tk.Entry(root, show="*")
    btn_login = tk.Button(root, text="Login", command=printInfo)
    btn_quit = tk.Button(root, text="Quit", command=root.quit)

    lab_logo.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
    lab_account.grid(row=1)
    lab_pwd.grid(row=2)
    entry_account.grid(row=1, column=1)
    entry_pwd.grid(row=2, column=1, pady=10)
    btn_login.grid(row=3, column=0)
    btn_quit.grid(row=3, column=1)

    root.mainloop()