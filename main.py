from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("icon/calculator.ico")  
root.geometry("310x530")
root.resizable(0, 0)

def negate():
    result=float(display.get()) *-1
    display.delete(0,END)
    display.insert(0,result)

def square():
    result=float(display.get()) ** 2
    display.delete(0,END)
    display.insert(0,result)

def inverse():
    if display.get()=="0":
        result = "ERROR"
    else:
        result = 1 / float(display.get())

    display.delete(0,END)
    display.insert(0,result)

def clearDisplay():
    display.delete(0,END)
    enableOperator()

def showNumber(number):
    display.insert(END,number)
    if "." in display.get():
        btnDecimal.config(state=DISABLED)

def equal():
    if operator=="add":
        result = float(firstNumber) + float(display.get())
    elif operator=="subtract":
        result = float(firstNumber) - float(display.get())
    elif operator=="multiply":
        result = float(firstNumber) * float(display.get())
    elif operator=="divide":
        if display.get()=="0":
            result="ERROR"
        else:
            result = float(firstNumber) / float(display.get())
    elif operator=="exponent":
        result = float(firstNumber) ** float(display.get())

    display.delete(0,END)
    display.insert(0,result)
    enableOperator()


def operation(value):
    global firstNumber
    global operator
    operator = value
    firstNumber = display.get()
    btnDecimal.config(state=NORMAL)
    display.delete(0,END)

    btnAdd.config(state=DISABLED)
    btnSubtract.config(state=DISABLED)
    btnMultiply.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnExponent.config(state=DISABLED)
    btnInverse.config(state=DISABLED)
    btnSquare.config(state=DISABLED)

def enableOperator():
    btnAdd.config(state=NORMAL)
    btnSubtract.config(state=NORMAL)
    btnMultiply.config(state=NORMAL)
    btnDivide.config(state=NORMAL)
    btnExponent.config(state=NORMAL)
    btnInverse.config(state=NORMAL)
    btnSquare.config(state=NORMAL)
    btnDecimal.config(state=NORMAL)

color = "#F79B72"
displayFont = ("Kanit", 35)
btnFont = ("Kanit", 19)

displayFrame = LabelFrame(root)
buttonFrame = LabelFrame(root)
displayFrame.pack(padx=2, pady=5)
buttonFrame.pack(padx=2)

display = Entry(displayFrame, width=30, font=displayFont, bg="#2A4759", fg="#EEEEEE", border=5, justify=RIGHT)
display.pack(padx=5, pady=5)

btnClear = Button(buttonFrame, text="Clear", font=btnFont, command=clearDisplay)
btnQuit = Button(buttonFrame, text="Quit", font=btnFont, command=root.destroy)
btnClear.grid(row=0, column=0, columnspan=2, ipadx=30, sticky="WE")
btnQuit.grid(row=0, column=2, columnspan=2, ipadx=30, sticky="WE")

btnInverse  = Button(buttonFrame, text="1/x", font=btnFont, bg=color)
btnSquare   = Button(buttonFrame, text="x^2", font=btnFont, bg=color)
btnExponent = Button(buttonFrame, text="x^n", font=btnFont, bg=color, command=lambda: operation("exponent"))
btnDivide   = Button(buttonFrame, text="/", font=btnFont, bg=color, command=lambda: operation("divide"))
btnMultiply = Button(buttonFrame, text="x", font=btnFont, bg=color, command=lambda: operation("multiply"))
btnSubtract = Button(buttonFrame, text="-", font=btnFont, bg=color, command=lambda: operation("subtract"))
btnAdd      = Button(buttonFrame, text="+", font=btnFont, bg=color, command=lambda: operation("add"))
btnEqual    = Button(buttonFrame, text="=", font=btnFont, bg=color, command=equal)
btnDecimal  = Button(buttonFrame, text=".", font=btnFont, bg=color, command=lambda: showNumber("."))
btnNegate   = Button(buttonFrame, text="+/-", font=btnFont, bg=color)

btn9 = Button(buttonFrame, text="9", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(9))
btn8 = Button(buttonFrame, text="8", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(8))
btn7 = Button(buttonFrame, text="7", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(7))
btn6 = Button(buttonFrame, text="6", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(6))
btn5 = Button(buttonFrame, text="5", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(5))
btn4 = Button(buttonFrame, text="4", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(4))
btn3 = Button(buttonFrame, text="3", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(3))
btn2 = Button(buttonFrame, text="2", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(2))
btn1 = Button(buttonFrame, text="1", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(1))
btn0 = Button(buttonFrame, text="0", font=btnFont, bg="#2A4759", fg="white", command=lambda: showNumber(0))

btnInverse.grid(row=1, column=0, pady=1, ipadx=10, sticky="WE")
btnSquare.grid(row=1, column=1, pady=1, ipadx=10, sticky="WE")
btnExponent.grid(row=1, column=2, pady=1, ipadx=10, sticky="WE")
btnDivide.grid(row=1, column=3, pady=1, ipadx=10, sticky="WE")

btn7.grid(row=2, column=0, padx=1, ipadx=10, sticky="WE")
btn8.grid(row=2, column=1, padx=1, ipadx=10, sticky="WE")
btn9.grid(row=2, column=2, padx=1, ipadx=10, sticky="WE")
btnMultiply.grid(row=2, column=3, padx=1, ipadx=10, sticky="WE")

btn4.grid(row=3, column=0, padx=1, ipadx=10, sticky="WE")
btn5.grid(row=3, column=1, padx=1, ipadx=10, sticky="WE")
btn6.grid(row=3, column=2, padx=1, ipadx=10, sticky="WE")
btnSubtract.grid(row=3, column=3, padx=1, ipadx=10, sticky="WE")

btn1.grid(row=4, column=0, padx=1, ipadx=10, sticky="WE")
btn2.grid(row=4, column=1, padx=1, ipadx=10, sticky="WE")
btn3.grid(row=4, column=2, padx=1, ipadx=10, sticky="WE")
btnAdd.grid(row=4, column=3, padx=1, ipadx=10, sticky="WE")

btnNegate.grid(row=5, column=0, padx=1, ipadx=10, sticky="WE")
btn0.grid(row=5, column=1, padx=1, ipadx=10, sticky="WE")
btnDecimal.grid(row=5, column=2, padx=1, ipadx=10, sticky="WE")
btnEqual.grid(row=5, column=3, padx=1, ipadx=10, sticky="WE")

root.mainloop()
