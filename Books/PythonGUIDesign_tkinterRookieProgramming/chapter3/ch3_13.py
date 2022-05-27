import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_13")
    root.geometry("300x180")

    label_ok = tk.Label(root, text="OK", fg="white",
                        bg="blue", font="Times 20 bold")
    label_no = tk.Label(root, text="NO", fg="white",
                        bg="red", font="Times 20 bold")
    label_ok.pack(anchor=tk.S, side=tk.RIGHT, padx=10, pady=10)
    # set in the sourth direction from the right and the spacing of y-axis is 10
    label_no.pack(anchor=tk.S, side=tk.RIGHT, pady=10)

    root.mainloop()