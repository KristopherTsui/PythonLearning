import tkinter as tk


def message_show():
    """ When the fuction button is clicked, the string "I love Python" can be 
    displayed". The background color is light yellow, and the string color is 
    blue.
    """
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    

if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch4_1")

    label = tk.Label(root)
    btn = tk.Button(root, text="打印消息", command=message_show)
    label.pack()
    btn.pack()

    root.mainloop()