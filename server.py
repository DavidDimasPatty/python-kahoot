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
        #score server
        self.score=0 
        #score client
        self.score_client=0
        #client done
        self.client_done=False
        self.server_done=False
        #variable
        self.i=1
        self.state=False
        self.var= tk.IntVar(self,1)
        self.var2= tk.IntVar(self,1)
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
            
    def addpage(self,page):
        self.pagenum=page
        self.changepage()
    
    def page3(self):
        self.server_done=True
        if self.client_done==True:
            label3=tk.Label(root, text = 'Score Client: '+ str(self.score_client))
            label=tk.Label(root, text = 'Final Score of you:')
            label. config(bg="#CCF3EE")
            label3. config(bg="#CCF3EE")
            label2=tk.Label(root, text = str(self.score*10))
            label2. config(bg="#CCF3EE")
            button=tk.Button(root, text = 'Go To Home Page',command =lambda:[self.addpage(0)])
            label.pack(ipadx=10, ipady=10)
            label2.pack(ipadx=10, ipady=10)
            button.pack(ipadx=10, ipady=10)
            label3.pack(ipadx=10, ipady=10)
            self.quest=0
            self.opsinum=0
        else:    
            label3=tk.Label(root, text = "Wait for client...")
            label=tk.Label(root, text = 'Final Score of you:')
            label. config(bg="#CCF3EE")
            label2=tk.Label(root, text = str(self.score*10))
            label3. config(bg="#CCF3EE")
            label2. config(bg="#CCF3EE")
            button=tk.Button(root, text = 'Go To Home Page',state="disabled")
            label.pack(ipadx=10, ipady=10)
            label2.pack(ipadx=10, ipady=10)
            button.pack(ipadx=10, ipady=10)
            label3.pack(ipadx=10, ipady=10)
            self.quest=0
            self.opsinum=0
        
    def page1(self):
        self.server_done=False
        if self.state==False:
            label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
            label. config(bg="#CCF3EE")
            label2=tk.Label(root, text = 'WAIT FOR CLIENT TO CONNECT')
            label2. config(bg="#CCF3EE")
            button=tk.Button(root, text = 'Start', state="disabled")
            label.pack(ipadx=10, ipady=10)
            button.pack(ipadx=10, ipady=10)
            label2.pack(ipadx=10, ipady=10)
        else:
            label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
            label. config(bg="#CCF3EE")
            button=tk.Button(root, text = 'Start', command =lambda:[self.addpage(1)])
            label.pack(ipadx=10, ipady=10)
            button.pack(ipadx=10, ipady=10)  
            self.score=0
      
     #checkjawaban
    def checkjawab(self,opsi,jawaban):
         if opsi==jawaban:
             self.score=self.score+1 
          
     
    def label_waiting(self):
                for self.i in range(1,11):
                    if( self.pagenum<=1):
                        break
                
                    elif self.pagenum >=1 and self.pagenum <=11 :
                            self.label1=tk.Label(root, text = str(self.i))
                            self.label1. config(bg="#CCF3EE")
                            self.label1.place(relx=0.5, rely=0.5, anchor="center")
                            self.waithere2()
                            self.label1.destroy()
                            
                    if(self.i==10):
                        self.changepage()
                        break
    #page soal
    def page2(self):
        label=tk.Label(root, text = self.pertanyaan[self.quest])
        label. config(bg="#CCF3EE")
        button1=tk.Button(root, text = self.opsi[self.opsinum], command =lambda:[self.checkjawab(self.opsi[self.opsinum-4],self.jawaban[self.quest-1]),self.cancel(),self.changepage()])
        button2=tk.Button(root, text = self.opsi[self.opsinum+1], command = lambda:[self.checkjawab(self.opsi[self.opsinum+1-4],self.jawaban[self.quest-1]), self.cancel(),self.changepage()])
        button3=tk.Button(root, text = self.opsi[self.opsinum+2], command = lambda:[self.checkjawab(self.opsi[self.opsinum+2-4],self.jawaban[self.quest-1]), self.cancel(),self.changepage()])
        button4=tk.Button(root, text = self.opsi[self.opsinum+3], command = lambda:[self.checkjawab(self.opsi[self.opsinum+3-4],self.jawaban[self.quest-1]), self.cancel(),self.changepage()])
        label.place(relx=0.5, rely=0.1, anchor="center")
        button1.place(relx=0.1, rely=0.2, anchor="nw")
        button2.place(relx=0.1, rely=0.3, anchor="nw")
        button3.place(relx=0.8, rely=0.2, anchor="ne")
        button4.place(relx=0.8, rely=0.3, anchor="ne")
        self.quest=self.quest+1
        self.opsinum=self.opsinum+4
        self.pagenum=self.pagenum+1
        self.label_waiting()
        

    #router
    def changepage(self):
        print(self.pagenum)
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum  == 0:
                self.client_done==False
                self.page1()
            
        if self.pagenum  == 12:
            self.page3()
            
        if self.pagenum >=1 and self.pagenum <=11:
                #self.cancel()
                '''   if self.pagenum==11:
                        self.changepage()
                    else: '''
                label=tk.Label(root, text = 'Get Ready')
                label. config(bg="#CCF3EE")
                z=6
                if(self.pagenum==11):
                    label=tk.Label(root, text = 'Calculate Score')
                    label. config(bg="#CCF3EE")
                    z=4
                label.pack(ipadx=10, ipady=10)
                #loops for wait
                for i in range(1,z):
                        label1=tk.Label(root, text = str(i))
                        label1.pack(ipadx=10, ipady=10)
                        self.waithere()
                        label1.destroy()
                label.destroy()    
                self.page2()
                #self.label_waiting(True)
        
            
            #root.mainloop()
   
   #wait 
    def waithere(self):
        self.after(1000, self.var.set, 1)
        print("waiting...")
        self.wait_variable(self.var)
        
    def waithere2(self):
        var2= tk.IntVar(self,0)
        self.after(1000, var2.set, 1)
        print("waiting2...")
        self.wait_variable(var2)    
   #counter wait
   
    def cancel(self):
       self.after_cancel(self)
     
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
                elif msg=="soal":
                    soal=self.baca_file()
                    y = str(soal)
                    y = y.encode()
                    conn.send(y)
                elif msg=="log_client":
                    self.state=True    
                    self.changepage()
                    y = "Connect"
                    y = y.encode()
                    conn.send(y)
                    
                elif msg=="serverdone":
                         if self.server_done==False:
                            print(self.server_done)
                            y = str(self.server_done)
                            y = y.encode()
                            conn.send(y)
                         elif self.server_done==True:
                            print(self.server_done)
                            y = str(self.score*10)
                            y = y.encode()
                            conn.send(y)             
                    
                elif len(msg)>=5 and msg[0:5]=="score":
                    self.score_client=int(msg[6:len(msg)+1])
                    self.client_done=True
                    if(self.pagenum==12):
                        print("masuk")
                        self.changepage()
                        y = str(self.score*10)
                        y = y.encode()
                        conn.send(y)
                    else:
                        y = str("False")
                        y = y.encode()
                        conn.send(y)
                        
                elif msg == self.DISCONNECT_MESSAGE:
                    bye="Thank you comeback later!"
                    conn.send(bye.encode(self.FORMAT))
                    connected = False
                '''  else:
                    res=msg
                    conn.send(str(res).encode(self.FORMAT))     '''
                         

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
    root.configure(background='#CCF3EE')
    Server(root)