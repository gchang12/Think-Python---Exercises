import time

#1.

def after_epoch():
    # Number of seconds since January 1st, 1970.
    today=time.time()
    seconds=int(today%60)
    minutes=int((today//60)%60)
    hours=int((today//(60*60))%24)
    days=int(today//(60*60*24))
    """This function returns the number of days, hours, minutes, and seconds, since January the first of 1970."""
    print(days, " days,", hours, " hours,", minutes, " minutes, and", seconds, " seconds have passed since the epoch.")

#2.

def check_fermat1(a,b,c,n):
    """This function takes three real numbers and an integer greater than two as arguments, and tests the triple
    and the integer to see if it proves Fermat's Last Theorem."""
    if type(n)!=int or n<=2:
        print("Please enter an integer greater than two and try again.")
    elif a==0 or b==0 or c==0:
        print("We are looking for non-trivial solutions to the Last Theorem. None of a, b, or c can be zero.")
    elif a**n+b**n==c**n:
        print("Fermat was wrong. Those scum must check their work.")
    else:
        print("The theorem holds.")

def check_fermat2():
    """This function asks for three real numbers and an integer greater than two, then tests the triple
        and the integer to see if it proves Fermat's Last Theorem."""
    n=int(input("Please enter an integer greater than two:\n"))
    while n<=2:
        n=int(input("Please enter an integer GREATER THAN TWO:\n"))
    a=float(input("Please enter a non-zero real number for the value of 'a':\n"))
    b =float(input("Please enter a non-zero real number for the value of 'b':\n"))
    c =float(input("Please enter a non-zero real number for the value of 'c':\n"))
    while a==0:
        a = float(input("Please enter a NON-ZERO  real number for the value of 'a':\n"))
    while b==0:
        b = float(input("Please enter a NON-ZERO real number for the value of 'b':\n"))
    while c==0:
        c = float(input("Please enter a NON-ZERO real number for the value of 'c':\n"))
    if a ** n + b ** n == c ** n:
        print("Fermat was wrong.")
    else:
        print("The theorem holds.")

#3.

def is_triangle1(a,b,c):
    """This function takes three positive numbers as arguments, and sees if a triangle can be formed with side lengths
    equal to these numbers."""
    if type(a)!=int or type(b)!=int or type(c)!=int:
        print("All three of the parameters must be integers.")
    if a < 0 or b < 0 or c < 0:
        print("All three of the parameters also have to be non-negative.")
    if a+b>c and c+b >a and c+a>b:
        print("Yes. This, a triangle makes.")
    elif a+b==c or a+c==b or c+a==b:
        print("Arr, this is a degenerate triangle.")
    else:
        print("This is no triangle.")

def is_triangle2():
    """This function asks for three positive numbers as arguments, and sees if a triangle can be formed with side lengths
    equal to these numbers."""
    a=int(input("Please input a positive integer denoting the length of side 'a':\n"))
    b = int(input("Please input a positive integer denoting the length of side 'b':\n"))
    c = int(input("Please input a positive integer denoting the length of side 'c':\n"))
    while a<0:
        a=int(input("Please input a NON-NEGATIVE integer for side 'a':\n"))
    while b<0:
        b=int(input("Please input a NON-NEGATIVE integer for side 'b':\n"))
    while c<0:
        c=int(input("Please input a NON-NEGATIVE integer for side 'c':\n"))
    if a+b>c and c+b >a and c+a>b:
        print("Yes. This, a triangle makes.")
    elif a+b==c or a+c==b or c+a==b:
        print("Arr, this is a degenerate triangle.")
    else:
        print("This is no triangle.")
