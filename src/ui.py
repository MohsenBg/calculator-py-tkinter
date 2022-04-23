from tkinter import *
from PIL import Image, ImageTk
import os
curtrentDir = os.path.dirname(__file__)
app = Tk()

# ----------------------------------------
BackgroundCanvas = Canvas(app, bg='grey15', width=300,
                          height=500, highlightthickness=0)
imgPath = os.path.join(curtrentDir, "../assets/image/background.png")
image = Image.open(imgPath).resize((300, 500),
                                   Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
BackgroundCanvas.create_image(0, 0, image=photo, anchor='nw')
BackgroundCanvas.place(x=0, y=0)
# ----------------------------------------------


# Diplay

# -----------------------------------------------

def make_label(master, x, y, h, w):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)
    label = Label(f)
    label.pack(fill=BOTH, expand=1)
    return label


CaculateDisplay = make_label(
    app, 0, 0, 40, 290)

CaculateDisplay.config(
    text="",
    background="#14171e",
    fg="white",
    font=("Arial", 11),
    anchor="e"
)

Dispaly = make_label(
    app, 0, 50, 40, 290)

Dispaly.config(background="#14171e", fg="white",
               font=("Arial", 19), text="0", justify="center", anchor="e")
# -------------------------------------------------


# Buttons
def makeNormalBtn(master=app, text="", textColor="white", backgroundColor="#14171e",  fontSize=14, activeforeground="#00FFFF"):
    NormalBtn = Button(
        master,

        background=backgroundColor,
        highlightthickness=0,
        bd=0,
        text=text,
        foreground=textColor,
        activeforeground=activeforeground,
        activebackground=backgroundColor,
        cursor="hand2",
        font=("Arial", fontSize)
    )
    return NormalBtn


RowFrame = Frame(app, width=180, height=30, background="#14171e")
RowFrame.place(x=25, y=175)
btnAC = makeNormalBtn(RowFrame, "AC")
btnPercent = makeNormalBtn(RowFrame, "%")
btnBackspace = makeNormalBtn(RowFrame, "←", fontSize=18)
btnAC.place(x=0, y=0)
btnBackspace.place(x=70, y=-5)
btnPercent.place(x=140, y=0)

ColumnFrame = Frame(app, width=35, height=240, background="#14171e")
ColumnFrame.place(x=245, y=170)
btnDivision = makeNormalBtn(ColumnFrame, "÷", "#1fca70",  fontSize=18)
btnMultiplication = makeNormalBtn(
    ColumnFrame, "×", "#1fca70",  fontSize=18)
btnSubmission = makeNormalBtn(
    ColumnFrame, "−", "#1fca70", fontSize=18)
btnSum = makeNormalBtn(ColumnFrame, "+", "#1fca70", fontSize=18)


btnDivision.place(x=0, y=0)
btnMultiplication.place(x=0, y=67)
btnSubmission.place(x=0, y=136)
btnSum.place(x=0, y=205)

ColumnFrame = Frame(app, width=40, height=40, background="#1cc069")
ColumnFrame.place(x=244, y=444)
btnEqual = makeNormalBtn(ColumnFrame, "=",
                         backgroundColor="#1cc069", activeforeground="red", fontSize=19)
btnEqual.pack(fill=BOTH, expand=True)


numPadFrame = Frame(app, background="#1A1D24", height=250, width=180)
numPadFrame.place(x=30, y=230)
btn9 = makeNormalBtn(numPadFrame, "9", backgroundColor="#1A1D24",
                     fontSize=18)
btn8 = makeNormalBtn(numPadFrame, "8", backgroundColor="#1A1D24",
                     fontSize=18)
btn7 = makeNormalBtn(numPadFrame, "7", backgroundColor="#1A1D24",
                     fontSize=18)

btn6 = makeNormalBtn(numPadFrame, "6", backgroundColor="#1A1D24",
                     fontSize=18)
btn5 = makeNormalBtn(numPadFrame, "5", backgroundColor="#1A1D24",
                     fontSize=18)
btn4 = makeNormalBtn(numPadFrame, "4", backgroundColor="#1A1D24",
                     fontSize=18)

btn3 = makeNormalBtn(numPadFrame, "3", backgroundColor="#1A1D24",
                     fontSize=18)
btn2 = makeNormalBtn(numPadFrame, "2", backgroundColor="#1A1D24",
                     fontSize=18)
btn1 = makeNormalBtn(numPadFrame, "1", backgroundColor="#1A1D24",
                     fontSize=18)
btnDot = makeNormalBtn(numPadFrame, ".", backgroundColor="#1A1D24",
                       fontSize=25)
btn0 = makeNormalBtn(numPadFrame, "0", backgroundColor="#1A1D24",
                     fontSize=18)
btnSymmetric = makeNormalBtn(numPadFrame, "+/−", backgroundColor="#1A1D24",
                             fontSize=18)

btn9.place(x=140, y=5)
btn8.place(x=70, y=5)
btn7.place(x=0, y=5)

btn6.place(x=140, y=70)
btn5.place(x=70, y=70)
btn4.place(x=0, y=70)

btn3.place(x=140, y=140)
btn2.place(x=70, y=140)
btn1.place(x=0, y=140)

btnSymmetric.place(x=130, y=210)
btn0.place(x=70, y=210)
btnDot.place(x=0, y=200)
