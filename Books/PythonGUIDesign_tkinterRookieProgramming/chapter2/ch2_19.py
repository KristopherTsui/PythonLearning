import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_19")
    """
    create image objects with PhotoImage method
    >>> imageobj = PhotoImage(file="xxx.gif")
    only supports gif file formate
    """
    youtube_gif = tk.PhotoImage(file="../imgs/youtube.gif")
    label = tk.Label(root, image=youtube_gif)
    label.pack()

    root.mainloop()