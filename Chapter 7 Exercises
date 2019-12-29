import math

#1.

def mysqrt(a):
    """This loop was copied from section 7.5 of the book, as instructed."""
    if a<0:
        return None
    x=int(a)
    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
        x = y

def test_sq_rt(estf,truef,a):
    """This function prints a table comparing the true values of a series of non-negative integers to their estimates using
    the mysqrt in this program. It displays also the absolute differences of the estimates and the theoretical values."""
    ln1=4
    ln2=len("estimate")
    ln3=15
    ln4=len("true")
    print("a"," "*ln1,"estimate"," "*ln3,"true"," "*ln3,"diff")
    print("-"," "*ln1,"-"*ln2," "*ln3,"-"*ln4," "*ln3,"-"*ln1)
    k=1
    if a<0:
        return None
    while k<=int(a):
        print(k," "*(4-len(str(k))),estf(k)," "*((ln3+ln2)-len(str(estf(k)))),truef(k)," "*((ln3+ln4)-len(str(truef(k)))),
              abs(estf(k)-truef(k)))
        k+=1

test_sq_rt(mysqrt,math.sqrt,-5)

#2.

def eval_loop():
    """This function prompts the user to enter in values, print the evaluation of those values, and then returns the
    last value entered if he or she enters 'done'."""
    x = input("Please input an expression to evaluate. If you would like to end the process and return the last value printed, type in 'done'.\n")
    done="done"
    while x.lower()!=done:
        print(eval(x),"\n")
        y=x
        x = input("Please input an expression to evaluate. If you would like to end the process and return the last value printed, type in 'done'.\n")
        if x.lower()==done:
            return eval(y)
    return x

#3.

def estimate_pi(eps):
    """This function takes a tolerance, and returns an estimation of pi until it is within the tolerance of pi."""
    if eps<=0:
        return None
    total=0
    k=0
    factor=2*math.sqrt(2)/9801
    while True:
        total+=math.factorial(4*k)*(1103+26390*k)/(math.factorial(k)**4*396**(4*k))
        if abs((factor*total)**(-1)-math.pi)< eps:
            return (factor*total)**(-1)
        k+=1
