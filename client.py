from asyncio.windows_events import INFINITE
from cgitb import handler
import time as time
import tkinter as tk
import socket
from ast import literal_eval
from turtle import color
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pagenum=0
        self.quest=0
        self.var= tk.IntVar(self,1)
        self.var2= tk.IntVar(self,1)
        self.pagenum=0
        self.quest=0
        self.opsinum=0
        self.score=0
        self.Lines=""
        self.server_done="False"
        self.i=1
        
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
        self.label1=''   
        
        #client connect
        self.HEADER = 64
        self.PORT = 5050
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        #############
        
        #dapetin soal
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
    def addpage(self,page):
        self.pagenum=page
        self.changepage()
    
    def check_server(self):
        print(self.server_done)
        self.server_done=self.send("score:"+str(self.score*10))
        if(self.server_done!="False"):
            self.changepage()
    
    def page3(self):
        if self.server_done=="False":
            label=tk.Label(root, text = 'Final Score of you:')
            label3=tk.Label(root, text = 'Wait for server...')
            label2=tk.Label(root, text = str(self.score*10))
            button=tk.Button(root, text = 'Go To Home Page',state="disabled")
            label. config(bg="#CCF3EE")
            label2. config(bg="#CCF3EE")
            label3. config(bg="#CCF3EE")
            label.pack(ipadx=10, ipady=10)
            label2.pack(ipadx=10, ipady=10)
            button.pack(ipadx=10, ipady=10)
            label3.pack(ipadx=10, ipady=10)
           
        elif self.server_done!="False":   
            label=tk.Label(root, text = 'Final Score of you:')
            label3=tk.Label(root, text = 'Server Score:')
            label2=tk.Label(root, text = str(self.score*10))
            button=tk.Button(root, text = 'Go To Home Page',command =lambda:[self.addpage(0)])
            label. config(bg="#CCF3EE")
            label2. config(bg="#CCF3EE")
            label3. config(bg="#CCF3EE")
            label.pack(ipadx=10, ipady=10)
            label2.pack(ipadx=10, ipady=10)
            button.pack(ipadx=10, ipady=10)
            label3.pack(ipadx=10, ipady=10)
            #self.server_done=self.send("score:"+str(self.score*10))
        self.quest=0
        self.opsinum=0
        ''' while self.server_done=="False":
            time.sleep(1)
            self.server_done=self.send("score:"+str(self.score*10))
            print(self.server_done) '''
    
        
    def page1(self):
        first_send=self.send('log_client')
        label=tk.Label(root, text = 'Welcome to Kahoot, Click start to play!')
        label. config(bg="#CCF3EE")
        button=tk.Button(root, text = 'Start', command =lambda:[self.addpage(1)])
        label.pack(ipadx=10, ipady=10)
        button.pack(ipadx=10, ipady=10)  
        self.score=0
        self.server_done="False"
        
    ''' # Define a function to start the loop
    def on_start(self):
         self.state = True


    # Define a function to stop the loop
        def on_stop(self):
            self.state =False '''

        
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

            
    def label_waiting(self):
                print("masuk")
                for self.i in range(1,11):
                    if self.pagenum==11 or self.pagenum==12  :
                        break
                    print("masuk2")
                    print(self.pagenum)
                    if( self.pagenum<1):
                        break
                
                    elif self.pagenum >=1 and self.pagenum <=10 :
                            self.label1=tk.Label(root, text = str(self.i))
                            self.label1. config(bg="#CCF3EE")
                            self.label1.place(relx=0.5, rely=0.5, anchor="center")
                            self.waithere2()
                            self.label1.destroy()
                    if(self.i==10):
                        self.changepage()
                        break
                                   
                   
                      
                   
    def page2(self):
        label=tk.Label(root, text = self.pertanyaan[self.quest])
        button1=tk.Button(root, text = self.opsi[self.opsinum], command =lambda:[self.checkjawab(self.opsi[self.opsinum-4],self.jawaban[self.quest-1]),self.cancel(),self.changepage()])
        button2=tk.Button(root, text = self.opsi[self.opsinum+1], command = lambda:[self.checkjawab(self.opsi[self.opsinum+1-4],self.jawaban[self.quest-1]), self.cancel(),self.changepage()])
        button3=tk.Button(root, text = self.opsi[self.opsinum+2], command = lambda:[self.checkjawab(self.opsi[self.opsinum+2-4],self.jawaban[self.quest-1]), self.cancel(),self.changepage()])
        button4=tk.Button(root, text = self.opsi[self.opsinum+3], command = lambda:[self.checkjawab(self.opsi[self.opsinum+3-4],self.jawaban[self.quest-1]), self.cancel(),self.changepage()])
        label. config(bg="#CCF3EE")
        label.place(relx=0.5, rely=0.1, anchor="center")
        button1.place(relx=0.1, rely=0.2, anchor="nw")
        button2.place(relx=0.1, rely=0.3, anchor="nw")
        button3.place(relx=0.8, rely=0.2, anchor="ne")
        button4.place(relx=0.8, rely=0.3, anchor="ne")
        self.quest=self.quest+1
        self.opsinum=self.opsinum+4
        self.pagenum=self.pagenum+1
        self.label_waiting()
            
     #check jawaban
    def checkjawab(self,opsi,jawaban):
         if opsi==jawaban:
             self.score=self.score+1 
            
    def changepage(self):
        print(self.pagenum)
        for widget in root.winfo_children():
            widget.destroy()
        if self.pagenum  == 0:
                self.page1()
            
        elif self.pagenum  == 11:
            self.page3()
            self.update()
            while self.server_done=="False":
                self.after(1000, self.check_server())
                self.update()  
        elif self.pagenum >=1 and self.pagenum <=10:
                #self.cancel()
                '''   if self.pagenum==11:
                        self.changepage()
                    else: '''
                label=tk.Label(root, text = 'Get Ready')
                label. config(bg="#CCF3EE")
                z=6
                if(self.pagenum==11):
                    self.server_done=self.send("score:"+str(self.score*10))
                    label=tk.Label(root, text = 'Calculate Score')
                    label. config(bg="#CCF3EE")
                    z=4
                label.pack(ipadx=10, ipady=10)
                #loops for wait
                for i in range(1,z):
                        label1=tk.Label(root, text = str(i))
                        label1. config(bg="#CCF3EE")
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
          
 

if __name__ == "__main__":
    pagenum = 1
    root = tk.Tk()
    pagenum=0
    root.wm_geometry("400x400")
    root.title("Python Kahoot")
    root.configure(background='#CCF3EE')
    main_page=Page(root)
    main_page.changepage()
    root.mainloop()