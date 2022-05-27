import tkinter as tk


if __name__ == '__main__':
    bitMaps = ["error", "hourglass", "info", "questhead", "question",
                "warning", "gray12", "gray25", "gray50", "gray75"]

    root = tk.Tk()
    root.title("ch3_5_1")

    # list all bitmaps
    for bitmap in bitMaps:
        tk.Label(root, bitmap=bitmap).pack(side=tk.LEFT, padx=5)

    root.mainloop()