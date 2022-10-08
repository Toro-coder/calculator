from tkinter import *

# numbers displaying
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


# clear numbers displayed
def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

# equal command
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


class calculator1:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        #self.root.geometry('300x300')
        self.root.resizable(False, False)

        display = Entry(self.root, font=('calibri', 16, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                        bg='powder blue', justify="right").grid(columnspan=4)

        btn7 = Button(self.root, command=lambda: btnClick(7), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=7).grid(row=1, column=0)
        btn8 = Button(self.root, command=lambda: btnClick(8), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=8).grid(row=1, column=1)
        btn9 = Button(self.root, command=lambda: btnClick(9), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=9).grid(row=1, column=2)
        btnadd = Button(self.root, command=lambda: btnClick('+'), padx=16, pady=16, bd=8, bg='powder blue',
                        font=('Calibri', 16, 'bold'), text='+').grid(row=1, column=3)

        # row 2
        btn4 = Button(self.root, command=lambda: btnClick(4), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=4).grid(row=2, column=0)
        btn5 = Button(self.root, command=lambda: btnClick(5), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=5).grid(row=2, column=1)
        btn6 = Button(self.root, command=lambda: btnClick(6), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=6).grid(row=2, column=2)
        btnminus = Button(self.root, command=lambda: btnClick('-'), padx=16, pady=16, bd=8, bg='powder blue',
                          font=('Calibri', 16, 'bold'), text='-').grid(row=2, column=3)

        # row 3
        btn1 = Button(self.root, command=lambda: btnClick(1), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=1).grid(row=3, column=0)
        btn2 = Button(self.root, command=lambda: btnClick(2), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=2).grid(row=3, column=1)
        btn3 = Button(self.root, command=lambda: btnClick(3), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=3).grid(row=3, column=2)
        btnmultiply = Button(self.root, command=lambda: btnClick('*'), padx=16, pady=16, bd=8, bg='powder blue',
                             font=('Calibri', 16, 'bold'),text='*').grid(row=3, column=3)

        # row 4
        btn0 = Button(self.root, command=lambda: btnClick(0), padx=16, pady=16, bd=8, bg='powder blue',
                      font=('Calibri', 16, 'bold'), text=0).grid(row=4, column=0)
        btnclear = Button(self.root, command=lambda: btnClearDisplay(), padx=16, pady=16, bd=8, bg='powder blue',
                          font=('Calibri', 16, 'bold'), text='C').grid(row=4, column=1)
        btnequal = Button(self.root, padx=16, pady=16, bd=8, bg='powder blue', font=('Calibri', 16, 'bold'),
                          text='=', command=btnEqualsInput).grid(row=4, column=2)
        btndivision = Button(self.root, command=lambda: btnClick('/'), padx=16, pady=16, bd=8, bg='powder blue',
                             font=('Calibri', 16, 'bold'),text='/').grid(row=4, column=3)


root = Tk()
operator = ""
text_input = StringVar()
obj = calculator1(root)
root.mainloop()
