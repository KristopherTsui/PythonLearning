import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch3_23")
    root.geometry("300x180")
    # list the contents of the widget control before and after execution
    print("Before execution", root.pack_slaves())
    label_ok = tk.Label(root, text="OK", fg="white",
                        bg="blue", font="Times 20 bold")
    label_no = tk.Label(root, text="NO", fg="white",
                        bg="red", font="Times 20 bold")
    label_ok.pack(anchor=tk.S, side=tk.RIGHT, padx=10, pady=10)
    label_no.pack(anchor=tk.S, side=tk.RIGHT, pady=10)
    print("After execution", root.pack_slaves())

    root.mainloop()