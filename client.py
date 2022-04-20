import tkinter as tk
import socket
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pagenum=0
        self.quest=0
        #arrray pertanyaan
        self.pertanyaan=[]
        #arrray opsi
        self.opsi=[]
        #arrray jawaban
        self.jawaban=[]
        #custom
        root.option_add('*font', ('verdana', 12))
        #bacafile
        ''' self.baca_file() '''
        ''' print(self.pertanyaan)
        print(self.opsi)
        print(self.jawaban) '''      
        #client connect
        self.HEADER = 64
        self.PORT = 5050
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self,msg):
            message = msg.encode(self.FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(self.FORMAT)
            send_length += b' ' * (self.HEADER - len(send_length))
            self.client.send(send_length)
            self.client.send(message)
            return self.client.recv(2048).decode(self.FORMAT) 
        
    '''  def baca_file(self):
     file1 = open('quest.txt', 'r')
     Lines = file1.readlines()
     print(len(Lines)) 
     # Strips the newline character
     for i in range (0,len(Lines),6):
         self.pertanyaan.append(Lines[i].strip())
         self.opsi.append(Lines[i+1].strip())
         self.opsi.append(Lines[i+2].strip())
         self.opsi.append(Lines[i+3].strip())
         self.opsi.append(Lines[i+4].strip())
         self.jawaban.append(Lines[i+5].strip()) '''
            
         
        
    def page1(self):
        label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
        button=tk.Button(root, text = 'Start', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)

    def page2(self):
        Lines=self.send("soal")
        print(type(Lines))
        print(len(Lines))
        for i in range (0,len(Lines),6):
            self.pertanyaan.append(Lines[i].strip())
            self.opsi.append(Lines[i+1].strip())
            self.opsi.append(Lines[i+2].strip())
            self.opsi.append(Lines[i+3].strip())
            self.opsi.append(Lines[i+4].strip())
            self.jawaban.append(Lines[i+5].strip())
        label=tk.Label(root, text = self.pertanyaan[self.quest])
        button1=tk.Button(root, text = self.opsi[self.opsinum], command = self.changepage)
        button2=tk.Button(root, text = self.opsi[self.opsinum+1], command = self.changepage)
        button3=tk.Button(root, text = self.opsi[self.opsinum+2], command = self.changepage)        
        button4=tk.Button(root, text = self.opsi[self.opsinum+3], command = self.changepage)
        label.place(relx=0.5, rely=0.1, anchor="center")
        button1.place(relx=0.1, rely=0.2, anchor="nw")
        button2.place(relx=0.1, rely=0.3, anchor="nw")
        button3.place(relx=0.8, rely=0.2, anchor="ne")
        button4.place(relx=0.8, rely=0.3, anchor="ne")
        self.quest=self.quest+1
        self.opsinum=self.opsinum+3
        self.pagenum=self.pagenum+1
        if(self.pagenum==10):
            self.pagenum=0
            
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