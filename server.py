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
            
         
        
    def page1(self):
        label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
        button=tk.Button(root, text = 'Start', command = self.changepage)
        label.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)

    def page2(self):
        label=tk.Label(root, text = 'Pertanyaan')
        button1=tk.Button(root, text = 'A', command = self.changepage)
        button2=tk.Button(root, text = 'B', command = self.changepage)
        button3=tk.Button(root, text = 'C', command = self.changepage)        
        button4=tk.Button(root, text = 'D', command = self.changepage)
        label.place(relx=0.5, rely=0.1, anchor="center")
        button1.place(relx=0.1, rely=0.2, anchor="nw")
        button2.place(relx=0.1, rely=0.3, anchor="nw")
        button3.place(relx=0.8, rely=0.2, anchor="ne")
        button4.place(relx=0.8, rely=0.3, anchor="ne")

    def changepage(self):
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum == 1:
            self.page2()
            self.pagenum = 0
        elif self.pagenum  == 0:
            self.page1()
            self.pagenum = 1
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
                else:
                    res=eval(msg)
                    print(res)
                    conn.send(str(res).encode(self.FORMAT))    
                    
                if msg == self.DISCONNECT_MESSAGE:
                    bye="Thank you comeback later!"
                    conn.send(bye.encode(self.FORMAT))
                    connected = False

            print(f" Success Calculator From [{addr}]")
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