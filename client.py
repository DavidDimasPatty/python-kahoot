import time as time
import tkinter as tk
import socket
from ast import literal_eval
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pagenum=0
        self.quest=0
        self.var= tk.IntVar(self,1)
        self.pagenum=0
        self.quest=0
        self.opsinum=0
        self.score=0
        self.Lines=""
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
        self.get_soal()

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
    def page3(self):
        label=tk.Label(root, text = 'Final Score of you:')
        label2=tk.Label(root, text = str(self.score*10))
        button=tk.Button(root, text = 'Go To Home Page', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        label2.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)           
         
        
    def page1(self):
        label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
        button=tk.Button(root, text = 'Start', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)
    
    def get_soal(self):
        self.Lines=self.send("soal")
        self.Lines=literal_eval(self.Lines)
        for i in range (0,len(self.Lines),6):
            self.pertanyaan.append(self.Lines[i].strip())
            self.opsi.append(self.Lines[i+1].strip())
            self.opsi.append(self.Lines[i+2].strip())
            self.opsi.append(self.Lines[i+3].strip())
            self.opsi.append(self.Lines[i+4].strip())
            self.jawaban.append(self.Lines[i+5].strip())
             
    def page2(self):
        label=tk.Label(root, text = self.pertanyaan[self.quest])
        button1=tk.Button(root, text = self.opsi[self.opsinum], command =lambda:[self.checkjawab(self.opsi[self.opsinum-4],self.jawaban[self.quest-1]), self.changepage()])
        button2=tk.Button(root, text = self.opsi[self.opsinum+1], command = lambda:[self.checkjawab(self.opsi[self.opsinum+1-4],self.jawaban[self.quest-1]), self.changepage()])
        button3=tk.Button(root, text = self.opsi[self.opsinum+2], command = lambda:[self.checkjawab(self.opsi[self.opsinum+2-4],self.jawaban[self.quest-1]), self.changepage()])
        button4=tk.Button(root, text = self.opsi[self.opsinum+3], command = lambda:[self.checkjawab(self.opsi[self.opsinum+3-4],self.jawaban[self.quest-1]), self.changepage()])
        label.place(relx=0.5, rely=0.1, anchor="center")
        button1.place(relx=0.1, rely=0.2, anchor="nw")
        button2.place(relx=0.1, rely=0.3, anchor="nw")
        button3.place(relx=0.8, rely=0.2, anchor="ne")
        button4.place(relx=0.8, rely=0.3, anchor="ne")
        self.quest=self.quest+1
        self.opsinum=self.opsinum+4
        self.pagenum=self.pagenum+1
                 
     #check jawaban
    def checkjawab(self,opsi,jawaban):
         if opsi==jawaban:
             self.score=self.score+1 
         print(self.score)
         print(jawaban)  
         print(opsi)         
            
    def changepage(self):
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum >=1 and self.pagenum <=10 :
            label=tk.Label(root, text = 'Get Ready')
            
            label1=tk.Label(root, text = '1')
            label.pack(ipadx=10, ipady=10)
            label1.pack(ipadx=10, ipady=10)
            self.waithere()
            label1.destroy()
            label1=tk.Label(root, text = '2')
            label1.pack(ipadx=10, ipady=10)
            self.waithere()
            label1.destroy()
            label1=tk.Label(root, text = '3')
            label1.pack(ipadx=10, ipady=10)
            self.waithere()
            label1.destroy()
            label1=tk.Label(root, text = '4')
            label1.pack(ipadx=10, ipady=10)
            self.waithere()
            label1.destroy()
            label1=tk.Label(root, text = '5')
            label1.pack(ipadx=10, ipady=10)
            self.waithere()
            label1.destroy()
            #time.sleep(5)
            label.destroy()
            label1.destroy()
            self.page2()
        elif self.pagenum  == 0:
            self.page1()
            self.pagenum = 1
        elif self.pagenum  == 11:
            self.page3()
            self.pagenum = 0    
            self.quest=0
            self.opsinum=0
            self.score=0
        #root.mainloop()
   
   #wait 
    def waithere(self):
        self.after(1000, self.var.set, 1)
        print("waiting...")
        self.wait_variable(self.var)         
    

if __name__ == "__main__":
    pagenum = 1
    root = tk.Tk()
    pagenum=0
    root.wm_geometry("400x400")
    root.title("Python Kahoot")
    main_page=Page(root)
    main_page.changepage()
    root.mainloop()