import tkinter as tk


def yellow():
    """ Set the background color is yellow. """
    root.config(bg="yellow")


def blue():
    """ Set the background color is blue. """
    root.config(bg="blue")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_5")
    root.geometry("300x200")

    exit_btn = tk.Button(root, text="Exit", command=root.destroy)
    blue_btn = tk.Button(root, text="Blue", command=blue)
    yellow_btn = tk.Button(root, text="Yellow", command=yellow)
    exit_btn.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
    blue_btn.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
    yellow_btn.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()