### These are functions created to shorten the length of the programs below ###

def letter_check(something):
    """This function takes any argument,
    and returns TRUE if it is not of length one or is not a string."""
    return len(something)>1 or type(something)!=str

def input_string():
    """This function will prompt the user to input a sequence of letters to be added to a set,
    which will be returned upon termination of the function."""
    print("If you wish to quit, type in 'done'.")
    x = input("Please input a letter to be added to the list: \n")
    x = x.lower()
    s=set()
    while True:
        if x=='done':
            break
        while letter_check(x):
            x = input("Please input a STRING with just a SINGLE letter--or input 'resume' to resume input: \n")
            x = x.lower()
            if x == 'resume':
                break
        if x not in s:
            s.add(x)
        x = input("Please input a letter that is not contained in the list whose cardinality you wish to print: \n")
        x = x.lower()
    s.discard('resume')
    return s

def scatter_word(word):
    """This function takes a word as an argument,
    and returns a set containing all of the unduplicated letters used in the word."""
    if type(word)!=str:
        raise TypeError
    s=set()
    word=word.strip()
    word = word.lower()
    for a in word:
        if a not in s:
            s.add(a)
    return s

def statistics_report(sample,frequency,ls):
    x = input("Which one of these would you like to know about the sequence of generated words?\n"
              "(a) The number of words in the sequence and the frequency of words with the given criteria in the sequence.\n"
              "(b) What the sequence looks like.\nType in a letter corresponding to one of the options above. "
              "Type in anything else to terminate the user-input prompt.\n\n")
    x = x.lower()
    if x == 'a':
        print("There are ", sample, " words in the sequence.\nThere are", round(frequency*sample)," words with the chosen "
        "criteria.\nThe frequency of these words in the list is ", round(frequency * 100, 2), "%.\n")
        print("The program will now terminate.")
        y=input("Would you like to view the generated sequence? (y/n)\n")
        if y=='y':
            print("This is what the sequence of words looks like:\n", ls)
            print("The program will now terminate.\n")
    if x=='b':
        print("This is what the sequence of words looks like:\n", ls)
        y=input("Would you like to view the statistics generated from this sequence? (y/n)\n")
        if y=='y':
            print("There are ", sample, " words in the sequence.\nThere are", round(frequency * sample),
                  " words with the chosen "
                  "criteria.\nThe frequency of these words in the list is ", round(frequency * 100, 2), "%.\n")
            print("The program will now terminate.")

#1.

file=open("words.txt")

def print_if(wlist,criteria):
    """This function takes a word list and a criteria function as arguments,
    and prints words from a word list fulfilling a certain criteria."""
    for word in wlist:
        word=word.strip()
        word = word.lower()
        if criteria(word):
            print(word,"\n")

def length_over_20(word):
    """This function takes a word as an argument,
    and returns TRUE if its length exceeds twenty."""
    if type(word)!=str:
        raise TypeError
    word = word.strip()
    word = word.lower()
    return len(word.strip())>20

def print_over_20(wlist):
    """This function takes a word list as an argument,
    and prints all words in the list whose length exceeds twenty."""
    print_if(wlist,length_over_20)

#2.

def has_no_letter(word,letter):
    """This function takes a word and a string as arguments,
    and returns TRUE if the string cannot be found within the word."""
    if type(word)!=str or type(letter)!=str:
        raise TypeError
    word = word.strip()
    word = word.lower()
    letter=letter.lower()
    return letter not in word

def has_no_e(word):
    """This function takes a word as an argument,
    and returns TRUE if the letter 'e' cannot be found within the word."""
    if type(word)!=str:
        raise TypeError
    word = word.strip()
    word = word.lower()
    return 'e' not in word

def count_no_letter(wlist,letter):
    """This function takes a word list and a string as arguments,
    and prints the number of words without a given letter in the list and the frequency of such words in the list."""
    if type(letter)!=str:
        raise TypeError
    k=set()
    n=0
    for word in wlist:
        n+=1
        word = word.strip()
        word = word.lower()
        if has_no_letter(word,letter):
            k.add(word)
    statistics_report(n,len(k)/n,k)

def count_no_e(wlist):
    """This function takes a word list as an argument,
    and prints the frequency and number of words without an 'e' in the list."""
    return count_no_letter(wlist,"e")

#3.

def avoids(word):
    """This program takes a word as an argument,
    and prompts the user to input a set of letters; then it returns TRUE if none of the letters are in the word."""
    if type(word)!=str:
        raise TypeError
    word = word.strip()
    word = word.lower()
    s=input_string()
    w=scatter_word(word)
    return s.isdisjoint(w)

def count_avoid(wlist):
    """This function takes a word list as an argument,
    and returns the number of words in the list not containing letters given via user-input."""
    t=input_string()
    n=0
    for word in wlist:
        n+=1
        word = word.strip()
        word = word.lower()
        if t.isdisjoint(scatter_word(word)):
            t.add(word)
    statistics_report(n, len(t) / n, t)

"""Choosing the vowels will yield the set with the least amount of elements."""

#4.

def uses_only(word,s):
    """This function takes a word and a set as an argument,
    and then the program will return TRUE if the word uses only those letters from the set."""
    if type(word)!=str:
        raise TypeError
    w=scatter_word(word)
    return w.issubset(s)

def acefhlo(wlist):
    """This function takes as an argument a word list, prompts the user to input a sequence of strings,
    and returns a set consisting of words that use letters only from the user-generated list."""
    s=input_string()
    t=set()
    n=0
    for word in wlist:
        n+=1
        word = word.strip()
        word = word.lower()
        if uses_only(word,s):
            t.add(word)
    statistics_report(n, len(t) / n, t)

"""You can write 'Aloha, fool!' with just the letters in the name of the function."""

#5.

def uses_all(word,s):
    """This function takes a word and a set as an argument,
    and will return TRUE if the word uses all of the letters of that set at least once."""
    if type(word)!=str:
        raise TypeError
    word = word.strip()
    word = word.lower()
    w=scatter_word(word)
    return w.issuperset(s)

def vowels(wlist):
    """This function takes a word list as an argument, prompts the user to input a sequence of strings,
    and prints the number of words that use all letters from that sequence at least once."""
    s = input_string()
    t=set()
    n=0
    for word in wlist:
        n+=1
        word = word.strip()
        word = word.lower()
        if uses_all(word, s):
            t.add(word)
    statistics_report(n, len(t) / n, t)

"""There are 598 words in the file that use all five vowels."""
"""There are 42 words in the list that use all five vowels plus 'y'."""

#6.

def abcedarian(word):
    """This function takes a word as an argument,
    and returns TRUE if the word it takes as an argument is 'abcedarian'."""
    if type(word)!=str:
        raise TypeError
    word = word.strip()
    word = word.lower()
    if len(word)>=2:
        for i in range(len(word)-2):
            if word[i]>word[i+1]:
                return False
    return True

def how_many_abc(wlist):
    """This function takes a word list and calculates how many words are 'abcedarian', the frequency of such words,
    and then prints the result."""
    t=set()
    n=0
    for word in wlist:
        n+=1
        word = word.strip()f
        word = word.lower()
        if abcedarian(word):
            t.add(word)
    statistics_report(n, len(t) / n, t)

"""There are  1573  'abcedarian' words in the word list. About  1.3821402525283588 % of the words are 'abcedarian'."""
