import tkinter as tk


def printSelection():
    print(dict_cities[int_var.get()])


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_3")

    dict_cities = {0: "东京", 1: "纽约", 2: "巴黎", 3: "伦敦", 4: "香港"}
    int_var = tk.IntVar()
    int_var.set(5)
    tk.Label(root, text="选择最喜欢的城市",
            fg="blue", bg="lightyellow", width=30).pack()
    for val, city in dict_cities.items():
        tk.Radiobutton(root, text=city, variable=int_var,
                        value=val, command=printSelection).pack()
        
    root.mainloop()