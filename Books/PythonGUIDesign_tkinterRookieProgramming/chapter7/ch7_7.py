import tkinter as tk


def main():
    root = tk.Tk()
    root.title("ch7_7")
    lab = tk.Label(root, text="Please select sports you like",
                    fg="blue", bg="lightyellow", width=30)
    lab.grid(row=0)

    int_var1 = tk.IntVar()
    cbtn_NFL = tk.Checkbutton(root, text="football", variable=int_var1)
    cbtn_NFL.grid(row=1, sticky=tk.W)
    int_var2 = tk.IntVar()
    cbtn_MLB = tk.Checkbutton(root, text="baseball", variable=int_var2)
    cbtn_MLB.grid(row=2, sticky=tk.W)
    int_var3 = tk.IntVar()
    cbtn_NBA = tk.Checkbutton(root, text="basketball", variable=int_var3)
    cbtn_NBA.grid(row=3, sticky=tk.W)

    root.mainloop()


if __name__ == '__main__':
    main()