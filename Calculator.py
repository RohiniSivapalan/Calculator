from tkinter import *                        # Importing all of the Tkinter Library

#=======================================================Making the window================================================================

win = Tk()                                   # Creating an instance of TK() class. In Short, Making the window for our program

win.title("Calculator")                      # Sets the title of our window
 
win.resizable(False, False)                  # prevents the resizing of the window

#=========================================================Defining the Functions=========================================================

# button_press function gets the Value and updates the display everytime a button is pressed
def button_press(num):
    global exp
    exp= input_text.get()
    exp= str(exp) + str(num)
    input_text.set(exp)


# button_operator function gets the operator(+, -, /, *) puts it on the screen and tells the equal function about the operater pressed
def button_oper(opr):
    global exp
    exp = input_text.get()
    exp= str(exp) + str(opr)
    input_text.set(exp)
    global oper
    oper = opr


# clr_scr function clears the screen and the expression variable 
def clr_scr():
    global exp
    input_text.set("")
    exp = ""


# equal function is invoked when equal button is pressed, this function gets the expression from the display,
# splits it into two numbers, performs the calculation depending upon the operator selected in the button_oper fuction,
# and puts the result on screen updating our expression with result value
def equal(event):
    global display
    global oper
    global exp
    exp = input_text.get()
    input_text.set("")
    result = float(eval(exp))
    exp = result
    display.insert(0, result)
    input_text.set(result)


#===================================================Making the Display===================================================================

# making a frame for our Display, mainly for aesthetics
display_frame = LabelFrame(win, text="Calc by Rohini", relief=SUNKEN, padx=2, pady=2)
display_frame.grid(row=0, column=0, columnspan=4, padx=2, pady=4)

# This is the text variable of our Display, Its a String Variable and stores/displays the String on the Entry Widget(Display).
input_text = StringVar()

# An Entry Widget Used to Display text on the screen, This is our main display for the Calculator
display = Entry(display_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=22, bg="#eee", bd=0, justify=RIGHT)
display.pack(ipady= 12) 
# ipady is used here to make the display wider


#===================================================creating the buttons==================================================================

# Defining all the buttons of our Calculator, Here we can define the aesthetics, the text displayed by the buttons and the
# function they will execute when pressed

# Buttons with consistent padx value
button_1 = Button(win, padx=30, pady=30, text="1", bg="light blue", command=lambda: button_press(1))
button_2 = Button(win, padx=30, pady=30, text="2", bg="light blue", command=lambda: button_press(2))
button_3 = Button(win, padx=30, pady=30, text="3", bg="light blue", command=lambda: button_press(3))
button_4 = Button(win, padx=30, pady=30, text="4", bg="light blue", command=lambda: button_press(4))
button_5 = Button(win, padx=30, pady=30, text="5", bg="light blue", command=lambda: button_press(5))
button_6 = Button(win, padx=30, pady=30, text="6", bg="light blue", command=lambda: button_press(6))
button_7 = Button(win, padx=30, pady=30, text="7", bg="light blue", command=lambda: button_press(7))
button_8 = Button(win, padx=30, pady=30, text="8", bg="light blue", command=lambda: button_press(8))
button_9 = Button(win, padx=30, pady=30, text="9", bg="light blue", command=lambda: button_press(9))
button_0 = Button(win, padx=30, pady=30, text="0", bg="light blue", command=lambda: button_press(0))
button_add = Button(win, padx=30, pady=30, text="+", bg="pink", command=lambda: button_oper("+"))
button_sub = Button(win, padx=30, pady=30, text="- ", bg="pink", command=lambda: button_oper("-"))
button_div = Button(win, padx=30, pady=30, text="/ ", bg="pink", command=lambda: button_oper("/"))
button_mul = Button(win, padx=30, pady=30, text="* ", bg="pink", command=lambda: button_oper("*"))
button_equal = Button(win, padx=10, pady=30, text="=", bg="orange", command=lambda: equal(""))
button_clear = Button(win, padx=10, pady=30, text="C", bg="orange", command=clr_scr)
button_dec = Button(win, padx=10, pady=30, text=" .", bg="orange", command=lambda: button_press("."))


#===================================================putting buttons on screen===========================================================

# putting all the above defined buttons on screen using the grid method 

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1,columnspan=2)  # Adjusted column span for the equal button
button_clear.grid(row=4, column=1,columnspan=1)
button_dec.grid(row=4, column=2,columnspan=1)
button_mul.grid(row=4, column=3)  # Adjusted column for the multiplication button

#=========================================================================================================================================

# Binds the Enter button of the keyboard to our window and calls the equal function when Enter is pressed
win.bind("<Return>", equal)

# Keeps the Window opened and loops into our program, until Close window Button is Not pressed
win.mainloop()
