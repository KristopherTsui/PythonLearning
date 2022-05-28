import tkinter as tk


def message_show():
    label.config(text="I love Python", bg="lightyellow", fg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_9")

    label = tk.Label(root)
    gif_sun = tk.PhotoImage(file="../imgs/sun.gif")
    # put the image to the left of text inside the function button
    btn_show = tk.Button(root, image=gif_sun, text="Click Me",
                        compound=tk.LEFT, command=message_show)
    
    label.pack()
    btn_show.pack()

    root.mainloop()