from tkinter import *
class MyWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("MyTable Game")
        self.config(bg='#aaeecc')
        self.b=Button(self,text="Start",command=self.DrawButton,bg='orange',fg='blue',font='arial 20 bold',bd=2,relief=RAISED)
        self.b.grid(row=0,column=0,padx=5,pady=5,ipadx=15,ipady=5,sticky='nsew')
        self.DrawLabel()
        self.DrawButton()
        self.Expand()
    def DrawLabel(self):
        for i in range(1,11):
            l=Label(self,text=str(i),bg='orange',fg='blue',font='arial 20 bold',bd=2,relief=RAISED)
            l.grid(row=0,column=i,padx=5,pady=5,ipadx=15,ipady=5,sticky='nsew')
        for i in range(1,11):
            l=Label(self,text=str(i),bg='orange',fg='blue',font='arial 20 bold',bd=2,relief=RAISED)
            l.grid(row=i,column=0,padx=5,pady=5,ipadx=15,ipady=5,sticky='nsew')
    def DrawButton(self):
        self.lb=[]
        for i in range(1,11):
            for j in range(1,11):
                self.lb.append(Button(self,text='?',command=lambda t=(i,j):self.Result(t),bg='orange',fg='blue',font='arial 20 bold',bd=2,relief=RAISED))
                self.lb[-1].grid(row=i,column=j,padx=5,pady=5,ipadx=15,ipady=5,sticky='nsew')
    def Expand(self):
        for i in range(11):
            self.grid_rowconfigure(i,weight=1)
        for i in range(11):
            self.grid_columnconfigure(i,weight=5)
    def Result(self,t):
        self.lb[(t[0]-1)*10+t[1]-1]['text']=str(t[0]*t[1])

root=MyWindow()
root.mainloop()
