import shutil
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Upload Signature")
canvas = Canvas(root, width=400, height=200)
canvas.pack()


def fileuploadfunc():
    root.fileName = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    shutil.move(root.fileName, '.\\')


Label(root, text="Open A File")
Button(root, text="Open A File", command=fileuploadfunc, height=2, width=45).place(x=40, y=30)

root.mainloop()
