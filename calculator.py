from tkinter import*
import time
root=Tk()
root.title("CALCULATOR")
f=0
def display(x):
    global f
    if x=='=':
        try:
            s1.set(str(eval(s1.get())))
        except Exception as e:
            s1.set(str.upper(str(e)))
            f=1
    elif f==1:
         s1.set('')
    elif x=='C':
        s1.set('')

    elif x=='CE':

        s1.set(s1.get()[:-1])
    else:
        s1.set(s1.get()+x)
f=Frame(root,bg='powder blue')
s1=StringVar()
e=Entry(f,textvariable=s1,justify=RIGHT,font='arial 50 bold',bd=5,bg='#1199fa',relief=RAISED)
e.pack(expand=YES,fill=BOTH,padx=5,pady=5)
f.pack(expand=YES,fill=BOTH,padx=5,pady=5)
t=iter(['blue','blue','blue','blue','blue'])
for s in[['C','CE'],'789/','456*','123+','.0=-']:
    f=Frame(root,bg=next(t))
    for i in s:
        b=Button(f,text=i,font='arial 20 bold',bd=5,bg='#1199fa',command=lambda x=i:display(x),relief=RAISED)
        b.pack(side=LEFT,expand=YES,fill=BOTH,padx=5,pady=5)
    f.pack(expand=YES,fill=BOTH)
def xyz():
    l['text']=time.ctime()
    l.after(1000,xyz)
f=Frame(root,bg='purple')
l=Label(f,font='arial 20 bold',bd=5,bg='#1199fa',relief=RAISED)
l.pack(expand=YES,fill=BOTH,padx=5,pady=5)
f.pack(expand=YES,fill=BOTH,padx=5,pady=5)
xyz()



root.mainloop()
