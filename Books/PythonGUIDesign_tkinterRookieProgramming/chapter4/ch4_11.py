import tkinter as tk


def messageShow():
    label.config(text="I lvoe Python", bg="lightyellow", fg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_11")
    label = tk.Label(root)

    gif_sun = tk.PhotoImage(file="../imgs/sun.gif")
    btn_image = tk.Button(root, image=gif_sun, command=messageShow, cursor="star")

    label.pack()
    btn_image.pack()

    root.mainloop()