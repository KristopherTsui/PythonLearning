import tkinter as tk


def message_show():
    label.config(text="I lvoe Python", bg="lightyellow", fg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_8")

    label = tk.Label(root)
    gif_sun = tk.PhotoImage(file="../imgs/sun.gif")
    # overlay text "Click Me" with image sun.gif inside function button.
    btn_show = tk.Button(root, image=gif_sun, text="Click Me",
                        compound=tk.CENTER, command=message_show)
    
    label.pack()
    btn_show.pack()

    root.mainloop()