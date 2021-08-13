# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable

from tkinter import Tk

expression = ""


# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	root=Tk()

	# set the background colour of GUI window
	root.configure(background="gray")

	# set the title of GUI window
	root.title("CALCULATOR")


	# set the configuration of GUI window
	root.geometry('345x281')
	root.iconbitmap('calculator.ico')

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	# expression_field = Entry(root, textvariable=equation)
	expression_field = Entry(relief=RIDGE, textvariable=equation, bd=10, font=("Aerial", 20), bg="powder blue")

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	# expression_field.grid(columnspan=5, ipadx=90)
	expression_field.grid(columnspan=4, ipady=10, ipadx=10, sticky="nsew")

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(root, text=' 1 ', fg='black', bg='orange',command=lambda: press(1), height=2, width=7)
	button1.grid(row=2, column=0,sticky="nsew")

	button2 = Button(root, text=' 2 ', fg='black', bg='orange',command=lambda: press(2), height=2, width=7)
	button2.grid(row=2, column=1,sticky="nsew")

	button3 = Button(root, text=' 3 ', fg='black', bg='orange',command=lambda: press(3), height=2, width=7)
	button3.grid(row=2, column=2,sticky="nsew")

	button4 = Button(root, text=' 4 ', fg='black', bg='orange',command=lambda: press(4), height=2, width=7)
	button4.grid(row=3, column=0,sticky="nsew")

	button5 = Button(root, text=' 5 ', fg='black', bg='orange',command=lambda: press(5), height=2, width=7)
	button5.grid(row=3, column=1,sticky="nsew")

	button6 = Button(root, text=' 6 ', fg='black', bg='orange',command=lambda: press(6), height=2, width=7)
	button6.grid(row=3, column=2,sticky="nsew")

	button7 = Button(root, text=' 7 ', fg='black', bg='orange',command=lambda: press(7), height=2, width=7)
	button7.grid(row=4, column=0,sticky="nsew")

	button8 = Button(root, text=' 8 ', fg='black', bg='orange',command=lambda: press(8), height=2, width=7)
	button8.grid(row=4, column=1,sticky="nsew")

	button9 = Button(root, text=' 9 ', fg='black', bg='orange',command=lambda: press(9), height=2, width=7)
	button9.grid(row=4, column=2,sticky="nsew")

	button0 = Button(root, text=' 0 ', fg='black', bg='orange',command=lambda: press(0), height=2, width=7)
	button0.grid(row=5, column=0,sticky="nsew")

	plus = Button(root, text=' + ', fg='black', bg='orange',command=lambda: press("+"), height=2, width=7)
	plus.grid(row=2, column=3,sticky="nsew")

	minus = Button(root, text=' - ', fg='black', bg='orange',command=lambda: press("-"), height=2, width=7)
	minus.grid(row=3, column=3,sticky="nsew")

	multiply = Button(root, text=' * ', fg='black', bg='orange',command=lambda: press("*"), height=2, width=7)
	multiply.grid(row=4, column=3,sticky="nsew")

	divide = Button(root, text=' / ', fg='black', bg='orange',command=lambda: press("/"), height=2, width=7)
	divide.grid(row=5, column=3,rowspan=2,sticky="nsew")

	equal = Button(root, text=' = ', fg='black', bg='orange',command=equalpress, height=2, width=7)
	equal.grid(row=5, column=2,rowspan=2,sticky="nsew")

	clear = Button(root, text='Clear', fg='black', bg='orange',command=clear, height=2, width=7)
	clear.grid(row=5, column='1',rowspan=2,sticky="nsew")

	Decimal= Button(root, text='.', fg='black', bg='orange',command=lambda: press('.'), height=2, width=7)
	Decimal.grid(row=6, column=0,sticky="nsew")



	# Start the GUI

	root.mainloop()
