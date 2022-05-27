import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_39")
    root.geometry("640x480")

    night_png = tk.PhotoImage(file="../imgs/night.png")
    label = tk.Label(root, image=night_png)
    # place the pciture control from the relative position (0.1,0.1),
    # the relative size is (0.8,0.8),
    # but do not set relwidth parameter.
    label.place(relx=0.1, rely=0.1, relheight=0.8)

    root.mainloop()