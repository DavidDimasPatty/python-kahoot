import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pagenum=0
        self.quest=1
        
    def page1(self):
        label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
        button=tk.Button(root, text = 'To page 2', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)

    def page2(self):
        label=tk.Label(root, text = 'Pertanyaan')
        button1=tk.Button(root, text = 'To page 1', command = self.changepage)
        button2=tk.Button(root, text = 'To page 1', command = self.changepage)
        button3=tk.Button(root, text = 'To page 1', command = self.changepage)        
        button4=tk.Button(root, text = 'To page 1', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        button1.pack(ipadx=10, ipady=10)
        button2.pack(ipadx=10, ipady=10)
        button3.pack(ipadx=10, ipady=10)
        button4.pack(ipadx=10, ipady=10)

    def changepage(self):
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum == 1:
            self.page2()
            self.pagenum = 0
        elif self.pagenum  == 0:
            self.page1()
            self.pagenum = 1
            
    

if __name__ == "__main__":
    pagenum = 1
    root = tk.Tk()
    pagenum=0
    root.wm_geometry("400x400")
    root.title("Python Kahoot")
    main_page=Page(root)
    main_page.changepage()
    root.mainloop()