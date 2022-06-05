import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch8_7")
    
    msg = "Welcome to You Tube system!"
    gif_youtube = tk.PhotoImage(file="../imgs/youtube.gif")
    logo = tk.Label(root, image=gif_youtube, text=msg, compound=tk.BOTTOM)
    logo.pack()

    labFrame = tk.LabelFrame(root, text="数据验证")
    accountL = tk.Label(labFrame, text="Account")
    accountL.grid(row=0, column=0)
    pwdL = tk.Label(labFrame, text="Password")
    pwdL.grid(row=1, column=0)

    accountE = tk.Entry(labFrame)
    accountE.grid(row=0, column=1)
    pwdE = tk.Entry(labFrame, show="*")
    pwdE.grid(row=1, column=1, pady=10)
    labFrame.pack(padx=5, pady=5, ipadx=5, ipady=5)

    root.mainloop()