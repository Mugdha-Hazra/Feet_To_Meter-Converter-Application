# in this module we will build a graphical user interface(GUI) using tkinter.
# tkinter is the most popular module in python to build gui

from tkinter import Tk, Button, Label, DoubleVar, Entry
'''
#importing the module and some specic function of the module like
i)   Tk : it is a class which is used to create the application window.
ii)  Button : for creating buttons 
iii) lable : for creating lables
iv)  DoubleVar : so that we can use double type variable
v)   Entry : for taking input from user

'''
window = Tk()  # creating the application container to the application window (the application window is stored inside the variavle window)
# adding a title to the application window
window.title("Feet To Meter Converter App")
# it ia a configure function where we are only setting the background colour
window.configure(background="purple")
# geometry function where we can set the width and height of our application
window.geometry("350x350")
# in the resizable function we are restricting the user from changeing the height and width of our application
window.resizable(width=False, height=False)


def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)


def clear():
    ft_value.set("")
    mt_value.set("")


''' part - 2
where we will add some lables  entry widgets and buttons to uor code
'''
ft_lb1 = Label(window, text="Feet Input", bg="black", fg="white", width=15)

'''
    ft_lb1 is a variable where we will store the lable which we imported from the Tk module 
    which contains the specification like  
    window in which the lable contains
     then text that we wanted to add in the lable, 
     background colour ,
     then foreground colour (text colour)  and
      the lable width
      '''
ft_lb1.grid(column=0, row=0, padx=20, pady=30)
# grid function is used to positionthe lable inside the application function.
'''
padx=padding in x direction (adding some space horizontally)
pady=padding in y direction (adding some space vartically)
so we are positioning the lable variable in row=0 and column =0
the grid function works as tables with rows and columns
'''

# part - 3 creating the user input section for the feet

# ft_value is a doubleVar variable so that we can take double(float) type input.
ft_value = DoubleVar()
# entry is also imported fom tkinter module
ft_entry = Entry(window, textvariable=ft_value, width=15)
'''
here 
window : application window inside which the entry contain
text_variable : type of value that accepts from the user
width : width of the input space
'''
ft_entry.grid(column=1, row=0)
# grid function for setting the position of the input space

# delete function is used for deletion of the entry space after we launch the application so it delets from 0 till end
ft_entry.delete(0, 'end')

# creating lable for meter input(same as above)
mt_lb1 = Label(window, text="Meter Input", bg="black", fg="white", width=15)
mt_lb1.grid(column=0, row=1, padx=20, pady=30)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=15)
mt_entry.grid(column=1, row=1)
mt_entry.delete(0, 'end')

# creating the clear button and convert button
'''
here ve created a variable for convert button which we imported from tkinkermodule and used
1. window : for creating the button inside the application window
2. text : the text on the button
3. bg : for setting the background colour of the button
4. fg : for setting the text colour
5. width : for setting the width of the button
6. command : this is for function call like when we click a button it perform the function

'''
cvt_btn = Button(window, text="Convert", bg="blue",
                 fg="black", width=14, command=convert)
# grid to position the button inside the window
cvt_btn.grid(column=0, row=3, padx=15)

clr_btn = Button(window, text="CLEAR", bg="black",
                 fg="orange", width=14, command=clear)

clr_btn.grid(column=1, row=3, pady=15)


window.mainloop()
# its like calling the function .without the main loop functn we cannot see the applicatin
