import tkinter as tk


def message_show():
    label.config(text="I love Python", bg="lightyellow", fg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_6")

    label = tk.Label(root)
    gif_sun = tk.PhotoImage(file="../imgs/sun.gif")
    # use sun.gif image replace "print message" button
    btn_show = tk.Button(root, image=gif_sun, command=message_show)
    
    label.pack()
    btn_show.pack()

    root.mainloop()