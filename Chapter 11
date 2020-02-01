file=open("words.txt")

#1.

def compile_word(wl):
    """This function reads a word list and returns a dictionary containing those words stored as keys with the
    length of the words as their values."""
    d={}
    for word in wl:
        d[word.strip()]=len(word)
    return d

#2.

def inv_dict(d):
    """This function inverts a dictionary that it takes as an argument using the dictionary method 'setdefault'."""
    s={}
    for key in d.keys():
        val=d.setdefault(key)
        if val in s.keys():
            s[val]+=[key]
        else:
            s[val]=[key]
    return s

#3.

def ack(m,n):
    """This function takes two numbers m and n as paramters, and returns the Ackerman function at (a,b)."""
    if m==0:
        return n+1
    if m>0 and n==0:
        return ack(m-1,1)
    if m>0 and n>0:
        return ack(m-1,ack(m,n-1))

def ack1(m,n):
    known={(0,n):n+1}
    if (m,n) in known.keys():
        return known[(m,n)]

    res=ack1(m-1,ack(m,n-1))
    known[(m,n)]=res
    return res

#4.

def has_duplicates(l):
    """This function takes a list as a parameter and returns true if there are any duplicates."""
    d=dict()
    for name in l:
        name=str(name)
        name=name.strip()
        if name not in d.keys():
            d[name]=1
        else:
            return True
    return False

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

def rot_pair(wl):
    """This function takes a word-list and returns a dictionary containing all its rotate pairs."""
    d={}
    for element in wl:
        element=element.strip()
        d[element]=[]
        for i in range(25):
            rot=rotate_word(element, -(i+1))
            if rot in d.keys():
                d[element]+=[rot]
    s={}
    for key in d.keys():
        if d[key]:
            s[key]=d[key]
    return s

#6.

def create_n(wl,n):
    """This function creates a list of words with exactly n letters."""
    l=[]
    for word in wl:
        word=word.strip()
        if len(word)==n:
            l+=[word]
    return l

def create_last_n(l,n):
    """This function takes a list and a positive integer and returns a list containing the last n letters of each of
    ther words from the list."""
    s=[]
    for word in l:
        s+=[word[len(word)-n:]]
    return s

def count_dic(l):
    """This function takes a list and returns a dictionary with the words as keys and number of occurrences as values."""
    d={}
    for word in l:
        if word in d.keys():
            d[word]+=1
        else:
            d[word]=1
    return d

def rem_dup(d):
    """This function takes a dictionary and creates a new list containing only those elements that were duplicated."""
    t=[]
    for key in d.keys():
        if d[key]>1:
            t+=[key]
    return t

def find_hmphn(wl):
    """This function takes a word list and stores all words sharing the same last three letters as values in a key
    equal to those three letters."""
    exact5=create_n(wl,5)
    last3=create_last_n(exact5,3)
    dup=count_dic(last3)
    t=rem_dup(dup)
    s=[]
    for word in exact5:
        word=word.strip()
        let3=word[2:]
        if let3 in t:
            s+=[word]
    d={}
    for item in t:
        d[item]=[]
        for word in s:
            if item==word[2:]:
                d[item]+=[word]
    return d

test=find_hmphn(file)
print(test)
