import tkinter as tk


def message_show():
    label.config(text="I love Python", bg="lightyellow", fg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_7")

    label = tk.Label(root)
    gif_sun = tk.PhotoImage(file="../imgs/sun.gif")
    # put the sun.gif image above the text "Click Me"
    btn_show = tk.Button(root, image=gif_sun, command=message_show,
                        text="Click Me", compound=tk.TOP)
    
    label.pack()
    btn_show.pack()

    root.mainloop()