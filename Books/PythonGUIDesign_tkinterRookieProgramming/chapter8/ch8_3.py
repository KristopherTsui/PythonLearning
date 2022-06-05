import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch8_3")

    frameUpper = tk.Frame(root, bg="lightyellow")
    frameUpper.pack()
    btnRed = tk.Button(frameUpper, text="Red", fg="red")
    btnRed.pack(side=tk.LEFT, padx=5, pady=5)
    btnGreen = tk.Button(frameUpper, text="Green", fg="green")
    btnGreen.pack(side=tk.LEFT, padx=5, pady=5)
    btnBlue = tk.Button(frameUpper, text="Blue", fg="blue")
    btnBlue.pack(side=tk.LEFT, padx=5, pady=5)

    frameLower = tk.Frame(root, bg="lightblue")
    frameLower.pack()
    btnPurple = tk.Button(frameLower, text="Purple", fg="purple")
    btnPurple.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()