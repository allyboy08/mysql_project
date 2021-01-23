import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import *

mydb= mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',host='127.0.0.1',database='lifechoicesonline',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

#register function
def verify():
        name_verify = name.get()
        user_verify = use.get()
        pass_verify= passw.get()
        num_verify= numb.get()
        status_verify= scat.get()
        sql= "INSERT INTO users (full_name,username,password,phone_number,status) VALUES(%s,%s,%s,%s,%s)"
        val=(name_verify,user_verify,pass_verify,num_verify,status_verify)
        mycursor.execute(sql, val)
        mydb.commit()


        messagebox.showinfo("message","Successfully created")


window= Tk()
window.title("Login page")
window.geometry("450x450")
window.configure(background="lightgreen")

#labels and entries
fname = tk.Label(window, text="Full Name")
fname.place(x=50, y=20)

name = tk.Entry(window, width=35)
name.place(x=250, y=20, width=100)


user = tk.Label(window, text="Username")
user.place(x=50, y=50)

use = tk.Entry(window, width=35)
use.place(x=250, y=50, width=100)

lpass = tk.Label(window, text="Password")
lpass.place(x=50, y=80)

passw = tk.Entry(window, width=35)
passw.place(x=250, y=80, width=100)


lnum = tk.Label(window, text="Mobile-Number")
lnum.place(x=50, y=110)

numb = tk.Entry(window, width=35)
numb.place(x=250, y=110, width=100)

stat = tk.Label(window, text="Status")
stat.place(x=50, y=150)

scat= ttk.Combobox(window, width=35, value=["Employee", "Student", "Visitor"])
scat.place(x=250, y=150, width=100)

regbtn= tk.Button(window, text="Create User", bg="blue", command=verify)
regbtn.place(x=150, y=200, width=100)

def close():
    ext = messagebox.askyesno(title="?", message="are you sure, you want to exit?")
    if ext == True:
        window.destroy()
    else:
        return None

#exit button
exitbtn = Button(window, command=close, text="exit")
exitbtn.place(x=260, y=200)

window.mainloop()