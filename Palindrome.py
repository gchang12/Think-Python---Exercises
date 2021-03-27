#The following code is for a problem for #d of Chapter 6.

def first(word):
    """This function takes a word and returns its first letter."""
    return word[0]

def last(word):
    """This function takes a word and returns its last letter."""
    return word[-1]

def middle(word):
    """This function takes a word and returns its middle letter."""
    return word[1:-1]

def is_palindrome1(word):
    """This function takes a word and returns True if it is a palindrome, using recursion."""
    if type(word)!=str:
        raise TypeError
    word=word.lower()
    if len(word)==0:
        return True
    if word.startswith(last(word)) and len(word)<=3:
        return True
    if word.startswith(last(word)):
        word=word[1:len(word)-1]
        return is_palindrome(word)
    else:
        return False

def is_palindrome2(word):
    """This function takes a word and returns True if it is a palindrome, using recursion."""
    word=word.lower()
    for i in range(len(word)):
        if word[i]!=word[len(word)-1-i]:
            return False
    return True
