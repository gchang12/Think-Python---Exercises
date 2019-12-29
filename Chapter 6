#2.

def ack(m,n):
    """This function takes two numbers m and n as paramters, and returns the Ackerman function at (a,b)."""
    if m==0:
        return n+1
    if m>0 and n==0:
        return ack(m-1,1)
    if m>0 and n>0:
        return ack(m-1,ack(m,n-1))

#4.

def is_power(a,b):
    """This function checks to see if a is a power of b where a and b are real numbers."""
    #Gotta make sure nobody feels like dividing by zero.
    if b==0:
        raise ZeroDivisionError
    #If b==1, then a is always a power of b.
    if b==1:
        return True
    #The trivial case is handled. If a==0, then it is a power of any non-negative real number. Also, no need#
        #to worry about the case if (a,b)==(0,0) because we already checked if b==0 in the first line.#
    if a==0:
        return True
    #Notice these checks are done before the recursion, because otherwise the recursion will not do all the
        #checks.
    if a%b==0:
        return is_power(a/b,b)
    #If a is a power of b, then dividing a by b some number of times will eventually reduce it via TDA to a==1.
    if a==1:
        return True
    else:
        return False

#5.

def gcd1(a,b):
    """This function takes two integers as arguments and returns their greatest common divisor, with recursive methods."""
    #Gotta check if arguments are integers.
    if type(a)!=int or type(b)!=int:
        raise TypeError
    #If both a and b are zero, then anything and everything (except zero) divides it.
    if a==0 and b==0:
        return None
    #These checks handle the trivial case where only one of a and b is zero.
    if a==0 or b==0:
        return max(abs(a),abs(b))
    y=max(a,b)
    x=min(a,b)
    #If x divides y, then gcd(x,y)=x. If the remainder is one, then the two original numbers are relatively prime.
    if y%x==0 or x==1:
        return x
    #If not, we apply the division algorithm.
    if y%x!=0:
        return gcd(x,y%x)

def gcd2(a,b):
    """This function takes two integers as paramters, and calculates their GCD through iteration."""
    if type(a)!=int or type(b)!=int:
        raise TypeError
    x=max(a,b)
    y=min(a,b)
    for i in range(y):
        if x%(y-i)==0 and y%(y-i)==0:
            return True
    return False
