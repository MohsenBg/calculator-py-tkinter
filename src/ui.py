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
CaculateDisplay = Label(app, width=35, height=2, background="#14171e", fg="white",
                        font=("Arial", 11), text="", justify="center", anchor="e")

CaculateDisplay.place(x=0, y=10)
Dispaly = Label(app, width=20, height=2, background="#14171e", fg="white",
                font=("Arial", 19), text="0", justify="center", anchor="e")
Dispaly.place(x=0, y=50)
# -------------------------------------------------


# Buttons
def makeNoramlBtn(text="", textColor="white", backgroundColor="#14171e", width=4, height=8, fontSize=14, activeforeground="#00FFFF"):
    NormalBtn = Button(
        width=width,
        pady=height,
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


btnAC = makeNoramlBtn("AC")
btnPercent = makeNoramlBtn("%")
btnBackspace = makeNoramlBtn("←", fontSize=18)
btnAC.place(x=15, y=170)
btnBackspace.place(x=80, y=165)
btnPercent.place(x=150, y=170)


btnDivision = makeNoramlBtn("÷", "#1fca70", width=2, fontSize=18)
btnMultiplication = makeNoramlBtn("×", "#1fca70", width=2, fontSize=18)
btnSubmission = makeNoramlBtn("−", "#1fca70", width=2, fontSize=18)
btnSum = makeNoramlBtn("+", "#1fca70", width=2, fontSize=18)
btnEqual = makeNoramlBtn("=", width=1, height=2,
                         backgroundColor="#1cc069", activeforeground="red", fontSize=19)

btnDivision.place(x=240, y=170)
btnMultiplication.place(x=240, y=235)
btnSubmission.place(x=240, y=300)
btnSum.place(x=240, y=365)
btnEqual.place(x=245, y=445)


btn9 = makeNoramlBtn("9", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btn8 = makeNoramlBtn("8", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btn7 = makeNoramlBtn("7", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)

btn6 = makeNoramlBtn("6", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btn5 = makeNoramlBtn("5", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btn4 = makeNoramlBtn("4", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)

btn3 = makeNoramlBtn("3", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btn2 = makeNoramlBtn("2", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btn1 = makeNoramlBtn("1", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btnDot = makeNoramlBtn(".", backgroundColor="#1A1D24",
                       fontSize=25, width=2, height=3)
btn0 = makeNoramlBtn("0", backgroundColor="#1A1D24",
                     fontSize=18, width=2, height=3)
btnSymmetric = makeNoramlBtn("+/−", backgroundColor="#1A1D24",
                             fontSize=18, width=2, height=3)

btn9.place(x=160, y=240)
btn8.place(x=90, y=240)
btn7.place(x=25, y=240)

btn6.place(x=160, y=310)
btn5.place(x=90, y=310)
btn4.place(x=25, y=310)

btn3.place(x=160, y=375)
btn2.place(x=90, y=375)
btn1.place(x=25, y=375)

btnSymmetric.place(x=160, y=440)
btn0.place(x=90, y=440)
btnDot.place(x=25, y=425)
