import tkinter as tk


def printSelection():
    lab.config(text="你选的是"+str_var.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_6")

    gif_star = tk.PhotoImage(file="../imgs/star.gif")
    gif_moon = tk.PhotoImage(file="../imgs/moon.gif")
    gif_sun = tk.PhotoImage(file="../imgs/sun.gif")

    str_var = tk.StringVar()
    str_var.set("默认值")
    lab = tk.Label(root, text="这是默认值，尚未选择", bg="lightyellow", width=30)
    lab.pack()
    rb_star = tk.Radiobutton(root, text="星星", image=gif_star, compound=tk.RIGHT,
                        variable=str_var, value="星星", command=printSelection)
    rb_star.pack()
    rb_moon = tk.Radiobutton(root, text="月亮", image=gif_moon, compound=tk.RIGHT,
                        variable=str_var, value="月亮", command=printSelection)
    rb_moon.pack()
    rb_sun = tk.Radiobutton(root, text="太阳", image=gif_sun, compound=tk.RIGHT,
                        variable=str_var, value="太阳", command=printSelection)
    rb_sun.pack()

    root.mainloop()