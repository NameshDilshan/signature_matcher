
import tkinter as tk
import shutil
import cv2
from skimage.metrics import structural_similarity as ssim
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw


import mysql.connector


def loginfunc():
    global uname
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="mysql", database="signverification")
    mycursor = mysqldb.cursor()
    uname = e1.get()
    password = e2.get()

    sql = "select * from login where uname = %s and password = %s"
    mycursor.execute(sql, [(uname), (password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login Success")
        p2.show()
        return True
    else:
        messagebox.showinfo("", "Incorrect Username Or Password")
        return False


# def getuserdetailsfunc():
#     mysqldb = mysql.connector.connect(host="localhost", user="root", password="mysql", database="signverification")
#     mycursor = mysqldb.cursor()
#     sql = "select * from userprofile where uname = %s "
#     mycursor.execute(sql, "as")
#     results = mycursor.fetchone()
#     for row in results:
#         nameValue = row['name']
#         print(row['name'])

#     if results:
#         messagebox.showinfo("", "Login Success")
#         p2.show()
#         return True
#     else:
#         messagebox.showinfo("", "Incorrect Username Or Password")
#         return False


def edit():
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
    p5.show()
    # tk.destroy()


def release(evt):
    global mousePressed
    global last
    mousePressed = False
    last = None


def fileuploadfunc():
    root.fileName = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    # os.rename(root.fileName, "img01.png") 
    # os.replace(root.fileName, '.\\')
    shutil.copy(root.fileName, '.\\')
    p6.show()


def matchimages():
    ans = match(".\\img.png", ".\\img01.png")
    if ans > 80:
        message = "Signatures Matched " + str(ans) + " % Please Proceed !!"
        messagebox.showinfo("", message)
        edit()
        p2.show()
    else:
        message = "Signatures Matched " + str(ans) + "% Please try again"
        messagebox.showinfo("", message)
        p2.show()


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
        global e1
        global e2

        Label(self, text="Login Page", font="ar 15 bold").place(x=200, y=150)
        Label(self, text="UserName").place(x=100, y=210)
        Label(self, text="Password").place(x=100, y=240)
        e1 = Entry(self)
        e1.place(x=200, y=210)
        e2 = Entry(self)
        e2.place(x=200, y=240)
        e2.config(show="*")
        Button(self, text="Login", command=loginfunc, justify= "center", height=2, width=50).place(x=70, y=350)


def callback():
    root.unbind('<Visibility>')

def pagechangetofour():
    messagebox.showinfo("", "Please Validate your Signature to Proceed")
    p4.show()

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # self.bind('<Visibility>', getuserdetailsfunc)  
        #Label(self, text="User Profile", font="ar 15 bold").grid(row=0, column=3)
        Label(self, text="User Profile", font="ar 15 bold").place(x=200, y=150)
        
        global nameentry
        global nicentry
        global addressentry

        name = Label(self, text="Name").place(x=100, y=210)
        nic = Label(self, text="NIC").place(x=100, y=240)
        address = Label(self, text="Address").place(x=100, y=270)

        # name.grid(row=1, column=5)
        # nic.grid(row=2, column=5)
        # address.grid(row=3, column=5)

        nameValue = StringVar()
        nicValue = StringVar()
        addressValue = StringVar()

        
        nameentry = Entry(self, textvariable=nameValue)
        nicentry = Entry(self, textvariable=nicValue)
        addressentry = Entry(self, textvariable=addressValue)

        nameValue.set("namesh")
        nicValue.set("1234567")
        addressValue.set("dsfasdfsdfsd")

        # nameentry.grid(row=4, column=7)
        # nicentry.grid(row=5, column=7)
        # addressentry.grid(row=6, column=7)
        nameentry.place(x=200, y=210)
        nicentry.place(x=200, y=240)
        addressentry.place(x=200, y=270)

        # Button(self, text="Edit", command=edit, justify= "center", height=2, width=50).place(x=70, y=350)
        Button(self, text="Validate Signature", command=pagechangetofour, justify= "center", height=2, width=50).place(x=70, y=350)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Please Validate your Signature to Proceed")
        label.pack(side="top", fill="both", expand=True)


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Please Draw your Signature and Save", font="ar 15 bold")
        label.pack(side="top", fill="both", expand=True)

        global canvas
        global mousePressed
        global last
        global img
        global draw

        canvas = Canvas(self, width=500, height=500, border=2)
        canvas.pack(side="top", fill="both", expand=True)

        img = Image.new('RGB', (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        mousePressed = False
        last = None
        canvas.bind_all('<ButtonPress-1>', press)
        canvas.bind_all('<ButtonRelease-1>', release)
        canvas.bind_all('<Motion>', move)
        Button(self, text="Save", command=save_image, height=2, width=50, justify= "center").place(x=70, y=350)


class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        global canvasx

        canvasx = Canvas(self, width=400, height=200)
        canvasx.pack()
        Label(self, text="Open A File")
        Button(self, text="Open A File", command=fileuploadfunc, justify= "center", height=2, width=50).place(x=70, y=350)
        # Button(self, text="Open A File", command=fileuploadfunc, height=2, width=45, justify= "center").place(x=40, y=30)


class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Button(self, text="Match Signatures", command=matchimages, justify= "center", height=2, width=50).place(x=70, y=350)
    #    Button(self, text="Match Signatures", command=matchimages, height=2, width=45, justify= "center").place(x=40, y=30)


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


        global p1
        global p2
        global p3
        global p4
        global p5
        global p6
        global p7
        global p8

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
        # buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Login Page", command=p1.show, state="disabled")
        b2 = tk.Button(buttonframe, text="User", command=p2.show)
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
