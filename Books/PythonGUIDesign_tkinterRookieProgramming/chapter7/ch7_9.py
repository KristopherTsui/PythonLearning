import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        self.boolRead = tk.BooleanVar()
        tk.Frame.__init__(self, master)
        self.createWidgets(master)

    def createWidgets(self, master):
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=0, columnspan=4,
                        padx=5, pady=5, sticky=tk.W)
        
        self.createButtons(master)

        self.boolRead.set(False)
        chkReadonly = tk.Checkbutton(master, text="只读",
                                    variable=self.boolRead, command=self.readonly)
        chkReadonly.grid(row=2, column=0)

    def createButtons(self, master):
        btnSel = tk.Button(master, text="选取", command=self.selectAll)
        btnSel.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        btnDeSel = tk.Button(master, text="取消选取", command=self.delSelect)
        btnDeSel.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        btnClr = tk.Button(master, text="删除", command=self.clear)
        btnClr.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        btnQuit = tk.Button(master, text="结束", command=master.destroy)
        btnQuit.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

    def selectAll(self):
        self.entry.select_range(0, tk.END)

    def delSelect(self):
        self.entry.select_clear()

    def clear(self):
        self.entry.delete(0, tk.END)

    def readonly(self):
        if self.boolRead.get() == True:
            self.entry.config(state=tk.DISABLED)
        else:
            self.entry.config(state=tk.NORMAL)


if  __name__ == '__main__':
    root = tk.Tk()
    root.title("ch7_9")
    app = Application(root)
    app.mainloop()