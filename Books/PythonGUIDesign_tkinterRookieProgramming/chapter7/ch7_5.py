import tkinter as tk


def printSelection():
    lab.config(text="你选择的是"+str_var.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_5")

    gif_star = tk.PhotoImage(file="../imgs/star.gif")
    gif_moon = tk.PhotoImage(file="../imgs/moon.gif")
    gif_sun = tk.PhotoImage(file="../imgs/sun.gif")

    str_var = tk.StringVar()
    str_var.set("默认值")

    lab = tk.Label(root, text="这是默认值，尚未选择", bg="lightyellow", width=30)
    rbStar = tk.Radiobutton(root, image=gif_star, variable=str_var,
                            value="星星", command=printSelection)
    rbMoon = tk.Radiobutton(root, image=gif_moon, variable=str_var,
                            value="月亮", command=printSelection)
    rbSun = tk.Radiobutton(root, image=gif_sun, variable=str_var,
                            value="太阳", command=printSelection)

    lab.pack()
    rbStar.pack()
    rbMoon.pack()
    rbSun.pack()

    root.mainloop()