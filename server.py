import tkinter as tk
from re import X
import socket 
import threading
from unittest import result

class Server(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pagenum=0
        self.quest=0
        self.opsinum=0
        self.score=0
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        #arrray pertanyaan
        self.pertanyaan=[]
        #arrray opsi
        self.opsi=[]
        #arrray jawaban
        self.jawaban=[]
        #custom
        root.option_add('*font', ('verdana', 12))
        #bacafile
        self.baca_file()
        print(self.pertanyaan)
        print(self.opsi)
        print(self.jawaban)  
        #start server    
        #self.start()
        self.changepage()
        threading.Thread(target=self.start,daemon=True).start()
        root.mainloop()
                
    def baca_file(self):
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
         self.jawaban.append(Lines[i+5].strip())
     ''' self.pertanyaan.append("batas")
     self.opsi.append("batas")
     self.opsi.append("batas")
     self.opsi.append("batas")
     self.opsi.append("batas")
     self.jawaban.append("batas") '''
     return Lines
            
    #page score       
    def page3(self):
        label=tk.Label(root, text = 'Final Score of you:')
        label2=tk.Label(root, text = str(self.score*10))
        button=tk.Button(root, text = 'Go To Home Page', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        label2.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)      
        
    #page welcome    
    def page1(self):
        label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
        button=tk.Button(root, text = 'Start', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)
        self.pagenum=0
      
     #checkjawaban
    def checkjawab(self,opsi,jawaban):
         if opsi==jawaban:
             self.score=self.score+1 
         print(self.score)
         print(jawaban)  
         print(opsi)       
     
      
    #page soal
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
        

    #router
    def changepage(self):
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum >=1 and self.pagenum <=10 :
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
     
    def handle_client(self,conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                if msg== "fail":
                    conn.send("WRONG INPUT FORMAT! TRY AND CHECK AGAIN".encode(self.FORMAT))
                if msg=="soal":
                    soal=self.baca_file()
                    y = str(soal)
                    y = y.encode()
                    conn.send(y)
                else:
                    res=eval(msg)
                    print(res)
                    conn.send(str(res).encode(self.FORMAT))    
                    
                if msg == self.DISCONNECT_MESSAGE:
                    bye="Thank you comeback later!"
                    conn.send(bye.encode(self.FORMAT))
                    connected = False

            #print(f" Success Calculator From [{addr}]")
        conn.close()       
    
    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}") 
        #buat manggil page
        #self.changepage()
        #ngejalanin tkinter
        while True: 
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            #self.quit()
              
    def _quit():
        root.quit()
        root.destroy()        
    


if __name__ == "__main__":
    pagenum = 1
    root = tk.Tk()
    pagenum=0
    root.wm_geometry("400x400")
    root.title("Python Kahoot Server")
    Server(root)