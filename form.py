import mysql.connector

from tkinter import *
from tkinter import messagebox
from subprocess import call


def edit():
    print(nameentry.get())
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="mysql", database="signverification")
    sql = "insert into userprofile (`name`, `nic`,`address`) VALUES ('"+nameentry.get()+"', '"+nicentry.get()+"', '"+addressentry.get()+"') "
    mycursor = mysqldb.cursor()
    mycursor.execute(sql)
    messagebox.showinfo("", "User Details Saved Successfully !! ")
    root.destroy()
    call(["python", "Main.py"])
    mysqldb.commit()
    mysqldb.close()
    mycursor.close()


root = Tk()
root.geometry("500x500")

Label(root, text="User Profile", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
nic = Label(root, text="NIC")
address = Label(root, text="Address")

name.grid(row=1, column=2)
nic.grid(row=2, column=2)
address.grid(row=3, column=2)

nameValue = StringVar
nicValue = StringVar
addressValue = StringVar

nameentry = Entry(root, textvariable=nameValue)
nicentry = Entry(root, textvariable=nicValue)
addressentry = Entry(root, textvariable=addressValue)

nameentry.grid(row=1, column=3)
nicentry.grid(row=2, column=3)
addressentry.grid(row=3, column=3)

Button(root, text="Edit", command=edit, height=3, width=13).place(x=10, y=100)
root.mainloop()
