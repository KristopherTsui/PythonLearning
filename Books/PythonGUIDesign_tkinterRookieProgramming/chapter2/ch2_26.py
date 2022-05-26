import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("ch2_26")
    my_title = "一个人的极境旅行"
    my_content = """2016年12月，我一个人订了机票和船票，开始我的南极旅行，
    飞机经迪拜再往阿根廷的乌斯怀亚，在此我登上游轮开始我的南极之旅。"""
    label1 = tk.Label(root, text=my_title, font="Helvetic 20 bold")
    label1.pack()
    sep = ttk.Separator(root, orient=tk.HORIZONTAL)
    # the divider fills the x-axis,
    # and it is 5 pixels from the window border to the left and right
    sep.pack(fill=tk.X, padx=5)
    label2 = tk.Label(root, text=my_content)
    label2.pack(padx=10, pady=10)
    root.mainloop()


if __name__ == '__main__':
    main()