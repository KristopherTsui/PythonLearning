import tkinter as tk


class AppCheckbutton(tk.Frame):

    def __init__(self, master=None):
        self.checkboxes = {}
        self.sports = {0: "Football", 1: "Baseball", 2: "Basketball", 3: "Tennis"}
        tk.Frame.__init__(self, master)
        self.createWidgets()

    def createWidgets(self, master=None):
        tk.Label(master, text="Please select sports you like", 
                fg="blue", bg="lightyellow", width=30).grid(row=0)

        for i in range(len(self.sports)):
            self.checkboxes[i] = tk.BooleanVar()
            tk.Checkbutton(master, text=self.sports[i],
                        variable=self.checkboxes[i]).grid(row=i+1, sticky=tk.W)

        btn = tk.Button(master, text="Confirm", width=10, command=self.printInfo)
        btn.grid(row=i+2)

    def printInfo(self):
        selection = ''
        for i in self.checkboxes:
            if self.checkboxes[i].get() == True:
                selection = selection + self.sports[i] + "\t"
        
        print(selection)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_8")
    app = AppCheckbutton(root)
    app.mainloop()