import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_35_2")
    # The zoom ratio is one when the window is resized.
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    
    label1 = tk.Label(root, text="Label 1", bg="pink")
    label2 = tk.Label(root, text="Label 2", bg="lightblue")
    label3 = tk.Label(root, bg="yellow")
    label1.grid(row=0, column=0, padx=5, pady=5, stick=tk.W)
    label2.grid(row=0, column=1, padx=5, pady=5)
    label3.grid(row=1, column=0, columnspan=2, padx=5,
                pady=5, sticky=tk.N+tk.S+tk.W+tk.E)
    root.mainloop()