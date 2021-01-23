from tkinter import *

import tkinter as tk
from datetime import *
from tkinter import messagebox





def verify():

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
window.geometry("500x500")
window.configure(background="lightgreen")

#date and time
date = datetime.now()
dlb = Label(window)
dlb.place(x=0, y=0)
dlb=date.strftime(" %H:%M")

logbtn = tk.Button(window, text="Login", bg="blue", command=verify)
logbtn.place(x=150, y=180, width=100)

regbtn = tk.Button(window, text="Register", bg="blue", command=sign)
regbtn.place(x=150, y=220, width=100)

#photo
photo= PhotoImage(file="life.png")
m=Label(window, image=photo)

m.place(x=0,y=0)

#admin hotkey
def opAd():
    import admin
    admin


window.bind("<Control-a>", lambda x: opAd())

adbtn = tk.Button(window, text="Admin", bg="blue", command=sign)
adbtn.place(x=150, y=260, width=100)

#exit button
def close():
    ext = messagebox.askyesno(title="?", message="are you sure, you want to exit?")
    if ext == True:
        window.destroy()
    else:
        return None

#exit button
exitbtn = Button(window, command=close, text="exit", bg="blue")
exitbtn.place(x=150, y=300,width=100)

window.mainloop()
