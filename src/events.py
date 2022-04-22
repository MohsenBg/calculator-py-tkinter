from ui import *
# didn't use Enum Because need use class
mode = "addNumber"

btn0.config(command=lambda: addNumber("0"))
btn1.config(command=lambda: addNumber("1"))
btn2.config(command=lambda: addNumber("2"))
btn3.config(command=lambda: addNumber("3"))
btn4.config(command=lambda: addNumber("4"))
btn5.config(command=lambda: addNumber("5"))
btn6.config(command=lambda: addNumber("6"))
btn7.config(command=lambda: addNumber("7"))
btn8.config(command=lambda: addNumber("8"))
btn9.config(command=lambda: addNumber("9"))

btnBackspace.config(command=lambda: backSpace())
btnAC.config(command=lambda: clearAll())

btnMultiplication.config(command=lambda: addOperator('×'))
btnDivision.config(command=lambda: addOperator('÷'))
btnSubmission.config(command=lambda: addOperator('−'))
btnSum.config(command=lambda: addOperator('+'))
btnEqual.config(command=lambda: result())
btnSymmetric.config(command=lambda: changeSignNumber())
btnDot.config(command=lambda: addDecimal())
btnPercent.config(command=lambda: Percent())


# add Number btn0 btn1 ... btn9
def addNumber(text: str):

    if(mode == "ERROR"):
        return
    finaltext = ""
    if(mode == "mustAddOperator"):
        return
    if len(Dispaly['text']) > 18 and mode == "addNumber":
        return

    elif Dispaly['text'] == "0" or mode == "addOperator" or mode == "result":
        finaltext = text
        changeMode("addNumber")

    else:
        finaltext = Dispaly['text']+text

    Dispaly.config(text=finaltext)
# ----------------------------------------------------


def addOperator(operator: str):

    finaltext = ""
    if(mode == "ERROR"):
        return

    if mode == "addOperator":
        finaltext = CaculateDisplay["text"][:-1]+operator

    elif mode == "result":
        finaltext = Dispaly['text']+operator

    elif mode == "mustAddOperator":
        finaltext = CaculateDisplay["text"]+operator

    else:
        sortedNumber = sortNumber(Dispaly['text'])
        finaltext = CaculateDisplay["text"]+sortedNumber+operator
        Dispaly.config(text=calc(CaculateDisplay["text"]+sortedNumber))

    changeMode("addOperator")
    CaculateDisplay.config(text=finaltext)


def calc(data: str):
    global mode
    result = ""
    try:
        data = data.replace("×", "*")
        data = data.replace("−", "-")
        data = data.replace("÷", "/")
        result = str(float(eval(data)))  # eval => float => str
        if(result[-2:] == ".0"):
            result = result[:-2]

        if(len(result) >= 18):
            indexE = result.find('e')

            if(indexE == -1):
                result = result[:18]

            else:
                result = result[:14]+result[indexE:]
    except:
        changeMode("ERROR")
        result = "ERROR"
    return result


def result():

    finaltext = ""
    if(mode == "ERROR"):
        return

    if(mode == "mustAddOperator"):
        finaltext = calc(CaculateDisplay['text'])

    else:
        finaltext = calc(CaculateDisplay['text']+Dispaly['text'])

    Dispaly.config(text=finaltext)
    CaculateDisplay.config(text="")
    changeMode("result")


def backSpace():

    if(mode == "ERROR"):
        return

    if(mode != "addNumber"):
        return

    if(len(Dispaly['text']) == 1):
        Dispaly.config(text="0")

    else:
        Dispaly.config(text=Dispaly['text'][:-1])


def clearAll():

    global mode
    CaculateDisplay.config(text="")
    Dispaly.config(text="0")
    mode = "addNumber"


def sortNumber(number: str):
    helper = number.replace("−", "-")

    if(float(helper)) > 0:
        return calc(number)

    else:
        return "(" + calc(number) + ")"


def changeSignNumber():

    finaltext = ""
    if(mode == "ERROR"):
        return

    if(Dispaly['text'] == "0" or mode == "mustAddOperator"):
        return

    elif(Dispaly['text'].find("−") == -1):
        finaltext = "−" + Dispaly["text"]

    else:
        finaltext = Dispaly["text"]
        finaltext = finaltext.replace("−", "")

    Dispaly.config(text=finaltext)


def addDecimal():

    finalText = ""

    if(mode == "ERROR"):
        return

    if(mode == "result" or mode == "addOperator"):
        finalText = "0."
        changeMode("addNumber")

    elif(Dispaly['text'].find('.') != -1):
        return

    else:
        finalText = Dispaly['text']+'.'
    Dispaly.config(text=finalText)


def Percent():

    if(mode == "ERROR"):
        return

    if not (mode == "addNumber" or mode == "result"):
        return
    number = float(Dispaly['text'])/100
    CaculateDisplay.config(text=CaculateDisplay['text'] + calc(str(number)))
    Dispaly.config(text=calc(CaculateDisplay['text']))
    changeMode("mustAddOperator")


def changeMode(modeStatus: str):
    global mode

    if(mode == "ERROR"):
        return

    if(modeStatus == "addNumber"):
        mode = "addNumber"

    elif(modeStatus == "addOperator"):
        mode = "addOperator"

    elif(modeStatus == "mustAddOperator"):
        mode = "mustAddOperator"

    elif(modeStatus == "ERROR"):
        mode = "ERROR"
