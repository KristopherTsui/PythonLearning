import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_15")

    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")
    label1.pack(fill=tk.X) # fill the X-axis
    # if the allocated container range is full, using the parameter has no effect.
    label2.pack(fill=tk.Y) 
    label3.pack(fill=tk.X) # fill the X-axis

    window.mainloop()