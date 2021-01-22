from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from datetime import *

mydb= mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',host='127.0.0.1',database='lifechoicesonline',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

def verify():
    user_verify = username.get()
    pass_verify= password.get()
    sql= "select * from users where username = %s and password = %s"
    mycursor.execute(sql, [(user_verify), (pass_verify)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo('Message', 'Logged in successfully')


        root = Tk()
        root.title("Sign-in Sign-out")
        root.geometry("250x100")
        signIn = datetime.now()
        x = signIn.strftime("%H:%M:%S")

        def signout():
            timeout = datetime.now()

            y = timeout.strftime("%H:%M:%S")
            z = username.get()

            timeInfo = z, x, y

            timeComm = "INSERT INTO sign_register(username, sign_in, sign_out) VALUES(%s, %s, %s)"

            mycursor.execute(timeComm, timeInfo)

            mydb.commit()
            messagebox.showinfo('Message', 'Signed out!')
            root.destroy()

        outbtn = Button(root, command=signout, text="Sign-Out")
        outbtn.place(x=10, y=10)

    else:
        messagebox.showinfo("message", "wrong login")








window= tk.Tk()
window.title("Login page")
window.geometry("450x450")
window.configure(background="lightgreen")

lbuse = tk.Label(window, text="Username")
lbuse.place(x=50, y=20)

username = tk.Entry(window, width=35)
username.place(x=250, y=20, width=100)

lbpass = tk.Label(window, text="Password")
lbpass.place(x=50, y=50)

password = tk.Entry(window, width=35, show="*")
password.place(x=250, y=50, width=100)

lnum = tk.Label(window, text="Mobile-Number")
lnum.place(x=50, y=80)

numb = tk.Entry(window, width=35)
numb.place(x=250, y=80, width=100)

logbtn= tk.Button(window, text="Login", bg="green", command=verify)
logbtn.place(x=50, y=135, width=55)

def close():
    ext = messagebox.askyesno(title="?", message="are you sure, you want to exit?")
    if ext == True:
        window.destroy()
    else:
        return None

#exit button
exitbtn = Button(window, command=close, text="exit")
exitbtn.place(x=120, y=135)

window.mainloop()