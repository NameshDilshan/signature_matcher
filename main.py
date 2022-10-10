# import tkinter as tk
# import mysql.connector
#
# from tkinter import *
#
# from login import ok
#
#
# class Demo1:
#
#     def __init__(self, master):
#         global e1
#         global e2
#         self.master = master
#         self.master.title("Login")
#         self.master.geometry("400x400")
#         self.frame = tk.Frame(self.master)
#         Label(self.master, text="UserName").place(x=10, y=10)
#         Label(self.master, text="Password").place(x=10, y=40)
#         e1 = Entry(self.master)
#         e1.place(x=140, y=10)
#
#         e2 = Entry(self.master)
#         e2.place(x=140, y=40)
#         e2.config(show="*")
#
#         Button(self.master, text="Login", command=ok, height=2, width=30).place(x=30, y=100)
#         # if canlogin:
#         #     app = Demo2(self.master)
#         #     self.master.mainloop()
#         # else:
#         #     self.master.destroy()
#         # self.butnew("Window 1", "ONE", Demo2)
#         # self.butnew("Window 2", "TWO", Demo3)
#         # self.frame.pack()
#
#     # def butnew(self, text, number, _class):
#     #     tk.Button(self.frame, text=text, width=25, command=lambda: self.new_window(number, _class)).pack()
#     #
#     # def new_window(self, number, _class):
#     #     self.newWindow = tk.Toplevel(self.master)
#     #     _class(self.newWindow, number)
#
# #
# # class Demo2:
# #     def __init__(self, master):
# #         self.master = master
# #         self.master.geometry("500x500")
# #
# #         Label(self.master, text="User Profile", font="ar 15 bold").grid(row=0, column=3)
# #
# #         name = Label(self.master, text="Name")
# #         nic = Label(self.master, text="NIC")
# #         address = Label(self.master, text="Address")
# #
# #         name.grid(row=1, column=2)
# #         nic.grid(row=2, column=2)
# #         address.grid(row=3, column=2)
# #
# #         nameValue = StringVar
# #         nicValue = StringVar
# #         addressValue = StringVar
# #
# #         nameentry = Entry(self.master, textvariable=nameValue)
# #         nicentry = Entry(self.master, textvariable=nicValue)
# #         addressentry = Entry(self.master, textvariable=addressValue)
# #
# #         nameentry.grid(row=1, column=3)
# #         nicentry.grid(row=2, column=3)
# #         addressentry.grid(row=3, column=3)
# #
# #         Button(self.master, text="Edit", command=edit, height=3, width=13).place(x=10, y=100)
# #         self.master.mainloop()
#
#
#
#         # self.frame = tk.Frame(self.master)
#         # self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
#         # self.label = tk.Label(master, text=f"this is window number {number}")
#         # self.label.pack()
#         # self.quitButton.pack()
#         # self.frame.pack()
#
#     # def close_windows(self):
#     #     self.master.destroy()
#
#
# # class Demo3:
# #     def __init__(self, master, number):
# #         self.master = master
# #         self.master.geometry("400x400+400+400")
# #         self.frame = tk.Frame(self.master)
# #         self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
# #         self.label = tk.Label(master, text=f"this is window number {number}")
# #         self.label.pack()
# #         self.label2 = tk.Label(master, text="THIS IS HERE TO DIFFERENTIATE THIS WINDOW")
# #         self.label2.pack()
# #         self.quitButton.pack()
# #         self.frame.pack()
# #
# #     def close_windows(self):
# #         self.master.destroy()
#
#
# def main():
#     tk = tk.Tk()
#     app = Demo1(tk)
#     tk.mainloop()
#
#
# if __name__ == '__main__':
#     main()

import tkinter as tk
import shutil
import cv2
from skimage.metrics import structural_similarity as ssim
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw

import mysql.connector


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


def edit():
    print(nameentry.get())
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="mysql", database="signverification")
    sql = "insert into userprofile (`name`, `nic`,`address`) VALUES ('" + nameentry.get() + "', '" + nicentry.get() + "', '" + addressentry.get() + "') "
    mycursor = mysqldb.cursor()
    mycursor.execute(sql)
    messagebox.showinfo("", "User Details Saved Successfully !! ")
    # root.destroy()
    # call(["python", "Main.py"])
    mysqldb.commit()
    mysqldb.close()
    mycursor.close()


def move(evt):
    global mousePressed
    global last

    x, y = evt.x, evt.y
    if mousePressed:
        if last is None:
            last = (x, y)
            return
        draw.line(((x, y), last), (0, 0, 0))
        canvas.create_line(x, y, last[0], last[1])
        last = (x, y)


def press(evt):
    global mousePressed
    mousePressed = True


def save_image():
    img.save('img.png')
    messagebox.showinfo("", "Image Saved Successfully !! ")
    # tk.destroy()


def release(evt):
    global mousePressed
    global last
    mousePressed = False
    last = None


def fileuploadfunc():
    root.fileName = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    shutil.copy(root.fileName, '.\\')


def matchimages():
    ans = match(".\\img.png", ".\\img01.png")
    if ans > 80:
        message = "Signatures Matched " + str(ans) + " % Please Proceed !!"
        messagebox.showinfo("", message)
    else:
        message = "Signatures Matched " + str(ans) + "% Please try again"
        messagebox.showinfo("", message)


def match(path1, path2):
    # read the images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    # turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # resize images for comparison
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    # display both images
    # cv2.imshow("One", img1)
    # cv2.imshow("Two", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    similarity_value = "{:.2f}".format(ssim(img1, img2) * 100)
    print("answer is ", float(similarity_value), "type=", type(similarity_value))
    return float(similarity_value)


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # label = tk.Label(self, text="This is page 2")
        global e1
        global e2

        Label(self, text="UserName").place(x=10, y=10)
        Label(self, text="Password").place(x=10, y=40)
        e1 = Entry(self)
        e1.place(x=140, y=10)
        e2 = Entry(self)
        e2.place(x=140, y=40)
        e2.config(show="*")

        Button(self, text="Login", command=ok, height=2, width=30).place(x=30, y=100)

        # label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Label(self, text="User Profile", font="ar 15 bold").grid(row=0, column=3)

        global nameentry
        global nicentry
        global addressentry

        name = Label(self, text="Name")
        nic = Label(self, text="NIC")
        address = Label(self, text="Address")

        name.grid(row=1, column=2)
        nic.grid(row=2, column=2)
        address.grid(row=3, column=2)

        nameValue = StringVar
        nicValue = StringVar
        addressValue = StringVar

        nameentry = Entry(self, textvariable=nameValue)
        nicentry = Entry(self, textvariable=nicValue)
        addressentry = Entry(self, textvariable=addressValue)

        nameentry.grid(row=1, column=3)
        nicentry.grid(row=2, column=3)
        addressentry.grid(row=3, column=3)

        Button(self, text="Edit", command=edit, height=3, width=13).place(x=10, y=100)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Please Validate your Signature to Proceed")
        label.pack(side="top", fill="both", expand=True)


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        global canvas
        global mousePressed
        global last
        global img
        global draw

        canvas = Canvas(self, width=500, height=500)
        canvas.pack(side="top", fill="both", expand=True)

        img = Image.new('RGB', (500, 500), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        mousePressed = False
        last = None
        canvas.bind_all('<ButtonPress-1>', press)
        canvas.bind_all('<ButtonRelease-1>', release)
        canvas.bind_all('<Motion>', move)
        Button(self, text="Save", command=save_image, height=2, width=50).place(x=70, y=350)


class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        global canvasx

        canvasx = Canvas(self, width=400, height=200)
        canvasx.pack()
        Label(self, text="Open A File")
        Button(self, text="Open A File", command=fileuploadfunc, height=2, width=45).place(x=40, y=30)


class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Button(self, text="Match Signatures", command=matchimages, height=2, width=45).place(x=40, y=30)


class Page7(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 7")
        label.pack(side="top", fill="both", expand=True)


class Page8(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 8")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)
        p7 = Page7(self)
        p8 = Page8(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)
        b4 = tk.Button(buttonframe, text="Page 4", command=p4.show)
        b5 = tk.Button(buttonframe, text="Page 5", command=p5.show)
        b6 = tk.Button(buttonframe, text="Page 6", command=p6.show)
        b7 = tk.Button(buttonframe, text="Page 7", command=p7.show)
        b8 = tk.Button(buttonframe, text="Page 8", command=p8.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        b7.pack(side="left")
        b8.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x500")
    root.mainloop()
