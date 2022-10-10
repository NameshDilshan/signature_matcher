import tkinter as tk
from tkinter import *
from tkinter import messagebox

import mysql.connector

root = tk.Tk()
root.geometry("400x400")

frame = tk.Frame(root)
frame.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
root.page1()

def ok():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="mysql", database="signverification")
    mycursor = mysqldb.cursor()
    uname = e1.get()
    password = e2.get()

    sql = "select * from login where uname = %s and password = %s"
    mycursor.execute(sql, [(uname), (password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login Success")
        # root.call("PYTHON", "form.py")
        # top = Toplevel()
        # top.mainloop()
        # root.destroy()
        # Page2.pack(root)

        return True

    else:
        messagebox.showinfo("", "Incorrect Username Or Password")
        return False


def page1():
        global e1
        global e2

        Label(root, text="UserName").place(x=10, y=10)
        Label(root, text="Password").place(x=10, y=40)
        e1 = Entry(root)
        e1.place(x=140, y=10)
        e2 = Entry(root)
        e2.place(x=140, y=40)
        e2.config(show="*")

        Button(root, text="Login", command=ok, height=2, width=30).place(x=30, y=100)

        # label.pack(side="top", fill="both", expand=True)


def page2():
    label = tk.Label(frame, text='this is the page2')
    label.place(relx=0.3, rely=0.4)


def page3():
    label = tk.Label(frame, text='this is the page3')
    label.place(relx=0.3, rely=0.4)


bt = tk.Button(root, text='page1', command=page1)
bt.grid(column=0, row=0)

bt1 = tk.Button(root, text='page2', command=page2)
bt1.grid(row=0, column=1)

bt2 = tk.Button(root, text='page3', command=page3)
bt2.grid(row=0, column=2)

root.mainloop()
