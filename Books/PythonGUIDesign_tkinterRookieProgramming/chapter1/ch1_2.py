import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("MyWindow") # set the window title to MyWindow
    root.geometry("300x160") # set the width to 300 and the height to 160
    root.configure(bg='yellow') # set the background color of the window to yellow
    root.mainloop()