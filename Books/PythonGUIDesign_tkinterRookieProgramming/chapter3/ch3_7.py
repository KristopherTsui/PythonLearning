import tkinter as tk


if __name__ == '__main__':
    window = tk.Tk()
    window.title("ch3_7")
    
    label1 = tk.Label(window, text="明志科技大学", bg="lightyellow")
    label2 = tk.Label(window, text="长庚大学", bg="lightgreen")
    label3 = tk.Label(window, text="长庚科技大学", bg="lightblue")
    # fill the x-axis and the y-axis is increased by 10 pixels
    label1.pack(fill=tk.X, pady=10)
    label2.pack(pady=10) # the y-axis is increased by 10 pixels
    label3.pack(fill=tk.X) # fill the x-axis packaging and positioning components

    window.mainloop()