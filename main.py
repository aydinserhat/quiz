import tkinter
from tkinter import *


screen = tkinter.Tk()
screen.title("BMI calculator")
screen.minsize(width=500 , height=500)
first_question = tkinter.Label(text="Enter Your Weight(kg):",font=('Arial',14,"italic"))
first_question.pack()
first_answer = tkinter.Entry(width=30)
first_answer.pack()
twice_question = tkinter.Label(text="Enter Your Height(cm):",font=('Arial',14,"italic"))
twice_question.pack()
result_label=tkinter.Label()
result_label.pack()
twice_answer = tkinter.Entry(width=30)
twice_answer.pack()
x=0
def calculated():
    w1= first_answer.get()
    h1= twice_answer.get()

    if w1 == "" or h1 == "":
        result_label.config(text="Enter your value")
    else:
        try:
            global x
            x = int(w1) / ((int(h1)*int(h1))/10000)
            result_string = sonuc(x)
            result_label.config(text=result_string)
        except:
            result_label.config(text="enter a valid number")


    print(x)
def sonuc(x):
        if x < 18.5:
            result = tkinter.Label(text=f"{x} Under weight ")
            result.pack()
        elif 18.5 < x < 24.99:
            result = tkinter.Label(text=f"{x} Normal weight ")
            result.pack()
        elif 25 < x < 29.99:
            result = tkinter.Label(text=f"{x} Over weight")
            result.pack()
        elif 30 < x < 34.99:
            result = tkinter.Label(text=f"{x} Obesit 1 weight ")
            result.pack()
        elif 35 < x < 39.99:
            result = tkinter.Label(text=f"{x} Obesit 2 weight ")
            result.pack()
        else:
            result = tkinter.Label(text=f"{x} Extreme Obesit weight ")
            result.pack()
        return result


calculate = tkinter.Button(text="Calculate",command=calculated)
calculate.pack()

screen.mainloop()