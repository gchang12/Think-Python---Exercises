#2.

def count_letter(word,a):
    """This function takes a word and string as parameters,
    and returns the number of occurrences of the string within the word."""
    if type(word)!=str or type(a)!=str or len(a)!=1:
        raise TypeError
    word=word.lower()
    a=a.lower()
    return word.count(a)

#3.

def is_sarah(word):
    """This function takes a string as a parameter and returns True if it is a palindrome."""
    if type(word)!=str:
        raise TypeError
    word=word.lower()
    return word==word[::-1]

#4. The reader is given a bunch of programs and is prompted to identify if it works as intended. If not, he or she is meant to state what it does instead.

"""Checks the first word in string 's' to see if it is lowercase."""

def anylower1(s):
    #Correct by removing 'else' statement and moving command to return False out of the loop.
    for c in s:
        if c.islower():
            return True
        else:
            return False

"""Returns the string (NOT BOOLEAN VALUE) 'True' for the string 'c'."""

def anylower2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"

"""Checks to see if the last letter of a string is lowercase."""

def anylower3(s):
    for c in s:
        flag=c.islower()
    return flag

"""Checks to see if any letter of string 's' is lowercase."""

def anylower4(s):
    flag=False
    for c in s:
        flag = flag or c.islower()
    return flag

"""Checks for the existence of any capital letters. If there are, it returns False."""

def anylower5(s):
    for c in s:
        if not c.islower():
            return False
    return True

#5.

def rotate_word(word,integer):
    """This program takes a word and an integer, and returns a word rotated by that integer. For example,
    'IBM' is 'HAL' rotated by 1."""
    if type(word)!=str or type(integer)!=int:
        raise TypeError
    s=""
    for letter in word:
        s+=chr(ord(letter)+integer)
    return s
