from tkinter import *

window = Tk()
window.title('CalculatorPro')
window.geometry('600x600')

InG1 = StringVar()

L = Label(text='Введите пример без знака "=":')
In = Entry(textvariable = InG1)
Res = Label(text='Результат: ???')
Btn = Button(text='Вычеслить')

def count(event):
    value = InG1.get()
    Res['text'] = 'Результат:', eval(value)
    
Btn.bind('<Button-1>', count)

L.pack()
In.pack()
Btn.pack()
Res.pack()

window.mainloop()
