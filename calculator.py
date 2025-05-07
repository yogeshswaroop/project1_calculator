from tkinter import *


expression = ""  # Global variable help to store the full expression of calculator

def get_digit(digit):
    global expression
    expression += str(digit)
    calculator_label.config(text=expression)  # now it will Update display

def clear():
    global expression
    expression = ""
    calculator_label.config(text="")  # it will Clear display

def get_operator(op):
    global expression
    if expression and expression[-1] not in "+-*/": 
        expression += op
        calculator_label.config(text=expression) 

def get_result():
    global expression
    try:
        result = eval(expression)  # Evaluate the full expression (it help to store all calculations)
        calculator_label.config(text=str(result))
        expression = str(result)  
    except ZeroDivisionError:
        calculator_label.config(text="Error")
        expression = ""
    except Exception:
        calculator_label.config(text="Invalid")
        expression = ""

root = Tk()
root.title('Calculator')
root.geometry("350x520")
root.resizable(0, 0)
root.configure(background="gray")

# *Calculator Display*
calculator_label = Label(root, text='', bg="black", fg="white", height=2, anchor="e", padx=10, relief=SUNKEN, bd=10)
calculator_label.grid(row=0, column=0, columnspan=1000, sticky='we', pady=(10, 10))
calculator_label.config(font=("Arial", 24, "bold"))


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    btn_style = {"width": 5, "height": 3, "font": ("Arial", 14, "bold"), "relief": RAISED, "bd": 5}
    
    if text.isdigit():
        btn = Button(root, text=text, bg='white', command=lambda t=text: get_digit(t), **btn_style)
    elif text == "C":
        btn = Button(root, text=text, bg='red', fg="white", command=clear, **btn_style)
    elif text == "=":
        btn = Button(root, text=text, bg='green', fg="white", command=get_result, **btn_style)
    else:
        btn = Button(root, text=text, bg='lightblue', command=lambda t=text: get_operator(t), **btn_style)

    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
