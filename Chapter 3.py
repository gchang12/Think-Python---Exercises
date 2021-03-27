#1.

def right_justify(a):
    """This is a function takes a string as an argument, and prints it
     so that its last character is the seventh character on the line."""
    spaces=" "*(70-len(a))
    print(spaces,a)

#2.

#Copied from the book...

def do_twice(f):
    """This function takes another function as an argument and then does that function twice."""
    f()
    f()

def print_spam():
    """This function prints the word 'spam'"""
    print("spam")

#Begin here:

def do_twice1(f,a):
    """This function takes another function and the parameter of that function as arguments,
    and then it executes that function twice."""
    f(a)
    f(a)

def print_twice(a):
    """This function takes a string as an argument, then prints it twice."""
    do_twice1(print,a)

def do_four(f):
    """This function takes a function as an argument, and then executes it four times."""
    do_twice(f)
    do_twice(f)

#3.

def do_n(f,n):
    """This function takes a function and a natural number 'n' as arguments,
    then executes the function 'n' times."""
    if type(n)!=int:
        raise TypeError
    elif n<0:
        raise IndexError
    for i in range(n):
        f()

def window(n):
    """This program creates a window with n**2 panes."""
    def border():
        print("+", " -" * n, end="  ")
    def side():
        print("| ", " " * n*2, end=" ")
    def more_sides():
        do_n(side, n)
        print("|")
    def pane():
        do_n(border,n)
        print("+")
        do_n(more_sides,n)
    do_n(pane,n)
    do_n(border,n)
    print("+")

def small_window():
    """"This function creates a window with sixteen panes."""
    def border():
        print("+ ","- "*2,end=" ")
    def side():
        print("| ","  "*2,end=" ")
    def pane():
        do_n(border,4)
        print("+")
        do_n(side, 4)
        print("|")
    do_n(pane,4)
    do_n(border, 4)
    print("+")
