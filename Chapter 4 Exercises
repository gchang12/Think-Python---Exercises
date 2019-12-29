import math
import turtle

adamantoise=turtle.Turtle()

def check_int(n):
    """This function takes any argument, and raises a type error if it is not an integer.."""
    if not type(n)==int or n<=0:
        raise TypeError

def square(length,t):
    """This function lakes a length and a turtle as arguments,
    then has the turtle trace a square with sides equal to that length."""
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(length,n,t):
    """This function takes a length, a positive integer, and a turtle as arguments,
    and draws a polygon with the amount of sides equal to that integer."""
    check_int(n)
    for i in range(n):
        t.lt(360/n)
        t.fd(length)

def circle(r,t):
    """This function takes a radius and turtle as arguments,
    then draws a circle with that radius."""
    n=50
    check_int(n)
    for i in range(n):
        t.lt(360/n)
        t.fd(2*math.pi*r/n)

def arc(r,ang,t):
    """This function takes a radius, an angle, and a turtle, and then it draws the arc of a circle with that radius,
    subtended by the angle."""
    n = 50
    for i in range(int(n*ang/360)):
        t.fd(2 * math.pi * r / n)
        t.rt(360 / n)

#2.

def petal(r,n,t):
    """This function takes a radius, an angle, and a turtle, and then it draws a petal to be used in iteration."""
    check_int(n)
    arc(r,180/n,t)
    t.rt(180-180/n)
    arc(r, 180 / n, t)
    t.lt(180-180/n)

def flower(r,n,t):
    """This function takes a radius, a natural number 'n', and a turtle as arguments, and then it draws a flower with
    'n' petals created with arcs subtended by the given radius."""
    check_int(n)
    for i in range(n):
        petal(r,n,t)

#3.

def slice(r,n,t):
    """This function takes a length, a natural number 'n', and a turtle as arguments, and then it draws a slice of an
    n-gon with side length equal to the given length."""
    check_int(n)
    ang=(180-360/n)/2
    side=2*math.sin(math.pi/n)*r
    t.fd(r)
    t.rt(180-ang)
    t.fd(side)
    t.rt(180-ang)
    t.fd(r)

def pie(r,n,t):
    """This function takes a length, a natural number 'n', and a turtle as arguments,
    and then it draws a pie with n slices whose short lengths are equal to the given length."""
    check_int(n)
    t.rt(360/n)
    for i in range(n):
        slice(r,n,t)
        t.rt(180)

#5.

def spiral(r,t):
    """This function takes a length and a turtle as arguments,
    and then it draws an Archimedean spiral of the given length."""
    n=100
    for i in range(n):
        t.lt(360/(i+1))
        t.fd(2*math.pi*r/(n+1))
