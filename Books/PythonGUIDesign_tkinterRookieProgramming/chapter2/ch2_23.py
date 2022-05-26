import tkinter as tk


def run_counter(digit):
    def counting():
        """ update number method.
        """
        global counter
        counter += 1
        digit.config(text=str(counter)) # list digital content
        digit.after(1000, counting) # call counting after one second
    counting() # keep calling


def main():
    root = tk.Tk()
    root.title("ch2_23")
    # black characters on a yellow background
    digit = tk.Label(root, bg="yellow", fg="blue",
                height=3, width=10, font="Helvetic 20 bold") # width 10 height 3
    digit.pack()
    run_counter(digit) # call the number update method

    root.mainloop()


if __name__ == '__main__':
    counter = 0 # global variable for count
    main()