import tkinter as tk
import tkinter.messagebox
import mysql.connector

s=''
try:
    db=mysql.connector.connect(host="localhost",username="root",password="root123",database="db")
    print("connection established")
except:
    print("connection failed")
cursor=db.cursor()

def fun():
    global s
    s=''
    a=e1.get()
    #cursor.execute("select * from songs where name like '%' " %a);
    cursor.execute("SELECT * FROM songs WHERE name LIKE %s ", ("%" + a + "%",))


    x=cursor.fetchone()
    """while x is not None:
        s=s+str(x)+'\n'
        x=cursor.fetchone()
    result.set(s)"""
    while x is not None:
        s=s+"Name : "+str(x[1])
        s=s+"\n\nLength of song : 0"+str(x[2])
        s=s+"\n\nVedio link : "+str(x[3])
        s=s+"\n\nType of song : "+str(x[4])
        s=s+"\n\nSinger : "+str(x[5])
        
        x=cursor.fetchone()
    result.set(s)
    
        
    
wn=tk.Tk()
wn.configure(bg="black")

e1=tk.Entry(wn,font=("calibria",15),fg="blue",justify="center")
e1.grid(row=0,columnspan=1,ipadx=10,ipady=10,sticky="we")

result=tk.StringVar(wn,value="Enter your song name")
l1=tk.Label(textvariable=result,justify="left",font=("calibria",15),fg="yellow",bg="black")
l1.grid(row=1,columnspan=1)

b1=tk.Button(text="Search",command=fun,font=("calibria",15),fg="blue",bg="yellow")
b1.grid(row=2,columnspan=1)

wn.mainloop()