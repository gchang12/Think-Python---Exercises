def check_int(n):
    """This function takes any argument, and raises a type error if it is not an integer.."""
    if not type(n)==int or n<=0:
        raise TypeError

#1.

def nested_sum(t):
    """This function takes a list of lists, and returns the sum of the values of the nested lists."""
    total=0
    for l in t:
        if type(l)!=list:
            raise TypeError
        else:
            total+=sum(l)
    return total

#2.

def cumulative_sum(t):
    """This function takes a list returns the list of the cumulative sum of the original list's values."""
    s=[]
    for i in range(len(t)):
        s+=[sum(t[:i+1])]
    return s

#3.

def middle(t):
    """This functions takes a list and returns it without the first and last elements."""
    if not t:
        return t
    if len(t)>1:
        t.pop(len(t)-1)
    t.pop(0)
    return t

#4.

def chop(t):
    """This function takes a list and removes its first and last elements."""
    if not t:
        return t
    if len(t) > 1:
        t.pop(len(t) - 1)
    t.pop(0)

#5.

def is_sorted(t):
    """This function takes a list and checks to see if it is sorted."""
    u=t.copy()
    t.sort()
    return t==u

#6.

def sort_letters(word):
    """This function takes a word and creates a sorted list of its letters."""
    if type(word)!=str:
        raise TypeError
    t=[]
    for a in word.lower():
        t+=[a]
    t.sort()
    return t

def is_anagram(word1,word2):
    """This function takes two words and returns True if they are anagrams."""
    word1=word1.lower()
    word2 = word2.lower()
    return sort_letters(word1)==sort_letters(word2)

hpcos1="TomMarvoloRiddle"
hpcos2="IAmLordVoldemort"

#7.

def has_duplicates(t):
    """This function takes a list and returns True if it contains any duplicated values."""
    s=[]
    for a in t:
        if a in s:
            return True
        else:
            s+=[a]
    return False

#8.

import random

def birthday_paradox(trial,student):
    """This function takes two positive integers as parameters: one for the sample size of students, and
    one for the number of trials. It returns the frequency that at least two students share the same birthday within
    a given sample size."""
    k=0
    check_int(trial)
    check_int(student)
    for j in range(trial):
        t=[]
        for i in range(student):
            t+=[random.randint(1,366)]
        if has_duplicates(t):
            k+=1
    return k/trial*100

#9.

import timeit

def read_wlist1(wordlist):
    """This function times the accumulator method of creating a list from a word list."""
    t=[]
    timer=timeit.timeit()
    for word in wordlist:
        t+=[word.strip()]
    return timer

def read_wlist2(wordlist):
    """This function times the append method of creating a list from a word list."""
    t=[]
    timer = timeit.timeit()
    for word in wordlist:
        t.append(word.strip())
    return timer

wordlist=open("words.txt")

def compare_methods(n):
    """This function is meant to compare which method is faster, based on how many trials 'n" to run."""
    acc=0
    check_int(n)
    total=0
    for i in range(n):
        m1=read_wlist1(wordlist)
        m2=read_wlist2(wordlist)
        total+=1
        if m1>m2:
            acc+=1
    print("The accumulator method took longer ",round(acc/total*100,2),"% of the time.")

#10.

def read_wlist(wordlist):
    """The accumulator method."""
    t=[]
    for word in wordlist:
        t+=[word.strip()]
    return t

def bisect_search(word,t):
    """This function takes a word and a list as arguments, and uses the bisection search method to determine if the
    word is in the list. If it is, it will return True."""
    half=int(len(t)/2)
    if len(t)==1:
        return True
    if word in t[:half]:
        return bisect_search(word,t[:half])
    elif word in t[half:]:
        return bisect_search(word,t[half:])
    else:
        return False

def reg_search(word,t):
    """Returns True if a word is in the list t."""
    return word in t

def compare_search(trials):
    """This function determines the percentage of instances that the bisection search runs faster
    than the normal method of search, using the given word list as an example."""
    k = 0
    t=read_wlist(wordlist)
    for j in range(trials):
        b=timeit.timeit()
        bisect_search(8,t)
        r = timeit.timeit()
        reg_search(8,t)
        if b >r:
            k+=1
    print("The bisection search method took longer ",k/trials*100,"% of the time")

#11.

def reverse_pair(wlist):
    """This function takes a word list and returns all reverse pairs in the list."""
    w=read_wlist(wlist)
    m=[]
    for word in w:
        m+=[word[::-1]]
    inter=list(set(w) & set(m))
    reverse=[]
    for element in inter:
        reverse+=[[element,element[::-1]]]
    return reverse

#12. Did not finish...

def interlock(word1,word2):
    """This function is meant to find all interlock pains in a word list. For example, if you take out all the odd
    letters of 'schooled' and put them in another word, you get two words: 'shoe' and 'cold'. These two words form an
    interlock pair."""
    if len(word1)!=len(word2):
        return None
    else:
        new_word=""
        for i in range(len(word1)-1):
            new_word+=word1[i]
            new_word+=word2[i]
    return new_word
