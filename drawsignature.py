from tkinter import *
from PIL import Image, ImageDraw

tk = Tk()
tk.title("Signature Please")
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

img = Image.new('RGB', (500, 500), (255, 255, 255))
draw = ImageDraw.Draw(img)

mousePressed = False

last = None


def press(evt):
    global mousePressed
    mousePressed = True


def save_image():
    img.save('img.png')
    tk.destroy()


def release(evt):
    global mousePressed
    global last
    mousePressed = False
    last = None


canvas.bind_all('<ButtonPress-1>', press)
canvas.bind_all('<ButtonRelease-1>', release)


def move(evt):
    global mousePressed, last
    x, y = evt.x, evt.y
    if mousePressed:
        if last is None:
            last = (x, y)
            return
        draw.line(((x, y), last), (0, 0, 0))
        canvas.create_line(x, y, last[0], last[1])
        last = (x, y)


canvas.bind_all('<Motion>', move)
Button(tk, text="Save", command=save_image, height=2, width=50).place(x=70, y=450)
tk.mainloop()
