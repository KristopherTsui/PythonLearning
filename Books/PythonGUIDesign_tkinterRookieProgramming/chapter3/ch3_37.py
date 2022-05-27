import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_37")
    root.geometry("640x480")
    night_png = tk.PhotoImage(file="../imgs/night.png")
    snow_png = tk.PhotoImage(file="../imgs/snow.png")
    label1 = tk.Label(root, image=night_png)
    label2 = tk.Label(root, image=snow_png)
    # set the position and size of the picture control directly in the window
    label1.place(x=20, y=30, width=200, height=120)
    label2.place(x=200, y=200, width=400, height=240)

    root.mainloop()