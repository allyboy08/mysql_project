from tkinter import *
import mysql.connector
import tkinter as tk
from datetime import *
from tkinter import messagebox


# mydb= mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',host='127.0.0.1',database='hospital',auth_plugin='mysql_native_password')
# mycursor=mydb.cursor()


def verify():
    # user_verify = username.get()
    # pass_verify= password.get()
    # sql= "select * from Login where username = %s and password = %s"
    # mycursor.execute(sql, [(user_verify), (pass_verify)])
    # results = mycursor.fetchall()
    if logbtn:
        window.withdraw()
        import login
        login.login()


def sign():
    if regbtn:
        window.withdraw()
        import regist
        regist


window = tk.Tk()
window.title("Login page")
window.geometry("700x700")
window.configure(background="lightgreen")

#date and time
date = datetime.now()
dlb = Label(window)
dlb.place(x=0, y=0)
dlb=date.strftime(" %H:%M")

logbtn = tk.Button(window, text="Login", bg="blue", command=verify)
logbtn.place(x=150, y=80, width=100)

regbtn = tk.Button(window, text="Register", bg="blue", command=sign)
regbtn.place(x=150, y=120, width=100)

#photo
# photo= PhotoImage(file="lifechoices.png")
# m=Label(window, image=photo)
#
# m.place(x=80,y=0)

def opAd():
    import admin
    admin


window.bind("<Control-a>", lambda x: opAd())

adbtn = tk.Button(window, text="Admin", bg="blue", command=sign)
adbtn.place(x=150, y=160, width=100)

#exit button
def close():
    ext = messagebox.askyesno(title="?", message="are you sure, you want to exit?")
    if ext == True:
        window.destroy()
    else:
        return None

#exit button
exitbtn = Button(window, command=close, text="exit", bg="blue")
exitbtn.place(x=150, y=200,width=100)

window.mainloop()
