import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch2_22")
    sse_text = """SSE 全名是 Silicon Stone Education，这家公司在美国，
    这是国际专业证照公司，产品多元与丰富。"""
    sse_gif = tk.PhotoImage(file="sse.gif")
    label = tk.Label(root, text=sse_text, image=sse_gif,
                    bg="lightyellow", compound="center")
    label.pack()

    root.mainloop()