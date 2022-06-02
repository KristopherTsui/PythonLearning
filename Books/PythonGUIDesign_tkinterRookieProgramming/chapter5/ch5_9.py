import tkinter as tk


def calculate():
    lab_out.configure(text="Result:"+str(eval(entry_equ.get())))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch5_9")
    
    lab_input = tk.Label(root, text="Please input math expression:")
    entry_equ = tk.Entry(root)
    lab_out = tk.Label(root)
    btn_cal = tk.Button(root, text="Calculate", command=calculate)

    lab_input.pack()
    entry_equ.pack(pady=5)
    lab_out.pack()
    btn_cal.pack(pady=5)

    root.mainloop()