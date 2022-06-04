import tkinter as tk


def printSelection():
    print(dict_cities[int_select.get()])


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_4")

    dict_cities = {0: "东京", 1: "纽约", 2: "巴黎", 3: "伦敦", 4: "香港"}
    int_select = tk.IntVar()
    int_select.set(5) # default not select
    tk.Label(root, text="选择最喜欢的城市", fg="blue",
            bg="lightyellow", width=30).pack()
    for val, city in dict_cities.items():
        ## replace option buttons with boxes
        tk.Radiobutton(root, text=city, indicatoron=0, width=30, value=val,
                        variable=int_select,  command=printSelection).pack()

    root.mainloop()