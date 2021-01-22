from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox


mydb= mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',host='127.0.0.1',database='lifechoicesonline',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()


def verify():
    try:
        user_verify = username.get()
        pass_verify= password.get()
        sql= "select * from admin where Username = %s and Password = %s"
        mycursor.execute(sql, [(user_verify), (pass_verify)])
        results = mycursor.fetchall()
        if results:
            table = Tk()
            table.title("Database tables")
            table.geometry("880x750")
            table.resizable(False,False)

            # SHOWING USERS IN A LIST BOX

            fname = Label(table, text="Full name")
            usernm = Label(table, text="Username")
            passwrd = Label(table, text="Password")


            fnamemList = Listbox(table, width=25)
            usernmList = Listbox(table, width=25)
            passwrdList = Listbox(table, width=25)

            # SHOWING SIGN IN/SIGN OUT TIMES IN A LIST BOX
            Username = Label(table, text="Username")
            signin = Label(table, text="Sign in")
            signout = Label(table, text="Sign out")

            usernamelist = Listbox(table, width=25)
            inlist = Listbox(table, width=25)
            outlist = Listbox(table, width=25)

            # FOR LOOPS (USERS LIST BOX)
            mycursor.execute("SELECT full_name from users")
            tab = mycursor.fetchall()

            for i in tab:
                fnamemList.insert(END, i)



            mycursor.execute("SELECT username from users")
            tab = mycursor.fetchall()

            for i in tab:
                usernmList.insert(END, i)



            mycursor.execute("SELECT status from users")
            tab = mycursor.fetchall()

            for i in tab:
                passwrdList.insert(END, i)



            # # FOR LOOPS FOR TIME REGISTER
            # mycursor.execute("SELECT username from sign_register")
            # tab = mycursor.fetchall()
            #
            # for i in tab:
            #     usernamelist.insert(END, i)

            mycursor.execute("SELECT sign_in from sign_register")
            tab = mycursor.fetchall()

            for i in tab:
                inlist.insert(END, i)

            mycursor.execute("SELECT sign_out from sign_register")
            tab = mycursor.fetchall()

            for i in tab:
                outlist.insert(END, i)

            fname.place(x=5, y=4)
            fnamemList.place(x=5, y=20)
            usernm.place(x=225, y=4)
            usernmList.place(x=225, y=20)
            passwrd.place(x=445, y=4)
            passwrdList.place(x=445, y=20)

            Username.place(x=5, y=210)
            usernamelist.place(x=5, y=225)
            signin.place(x=225, y=210)
            inlist.place(x=225, y=225)
            signout.place(x=445, y=210)
            outlist.place(x=445, y=225)

            table.mainloop()
        else:
            messagebox.showinfo('Error', 'Incorrect Password/Username')
            quit()
    except:
        pass

window= tk.Tk()
window.title("Login page")
window.geometry("450x250")
window.configure(background="lightgreen")



lbuse = tk.Label(window, text="Username")
lbuse.place(x=50, y=20)

username = tk.Entry(window, width=35)
username.place(x=250, y=20, width=100)

lbpass = tk.Label(window, text="Password")
lbpass.place(x=50, y=50)

password = tk.Entry(window, width=35, show="*")
password.place(x=250, y=50, width=100)

logbtn= tk.Button(window, text="Login", bg="green", command=verify)
logbtn.place(x=50, y=135, width=55)

window.mainloop()