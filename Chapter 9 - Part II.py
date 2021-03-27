#7.

wlist=open("words.txt")

def check_six(word):
    """This function checks to see if a word has three consecutive pairs of matching letters."""
    word=word.lower()
    #The condition fails immediately if the word has fewer than six letters.
    if len(word)<6:
        return False
    else:
        #The indexing is so we do not go out of range with the conditional on the next line.
        for i in range(len(word)-5):
            if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                return True
    return False

def print_six(wlist):
    """This function prints a list of words that have three consecutive pairs of matching letters."""
    for word in wlist:
        if check_six(word):
            print(word)
    #It's "bookkeeper", by the way.

#8.

def is_sarah(word):
    """This function takes a parameter and returns True if it is a palindrome."""
    return word==word[::-1]

def check_odo(num):
    """This function checks a positive integer that is at most a million, matching the criteria:
    (1) Last four digits is a palindrome.
    (2) After increment one, last five digits is a palindrome.
    (3) After increment two, middle four digits is a palindrome.
    (4) After increment 3, whole reading is a palindrome."""
    if type(num)!=int:
        raise TypeError
    else:
        s = str(num)
        s.zfill(6)
        #This check corresponds to (1).
        if is_sarah(s[3::]):
            s = str(num + 1)
            s=s.zfill(6)
            # This check corresponds to (2).
            if is_sarah(s[2::]):
                s = str(num + 2)
                s=s.zfill(6)
                # This check corresponds to (3).
                if is_sarah(s[1:5]):
                    s = str(num + 3)
                    s=s.zfill(6)
                    # This check corresponds to (4).
                    if is_sarah(s):
                        return True

def print_odo():
    """This function prints all possible odometer readings matching the criteria:
    (1) Last four digits is a palindrome.
    (2) After increment one, last five digits is a palindrome.
    (3) After increment two, middle four digits is a palindrome.
    (4) After increment 3, whole reading is a palindrome."""
    for i in range(999999):
        if check_odo(i):
            print(i)
    #It's 199999, by the way.

#9.

def check_age(age1,age2):
    """This function takes two ages less than a hundred and returns the amount of instances they are palindromes."""
    if type(age1)!=int or type(age2)!=int:
        raise TypeError
    else:
        #Notation should be straightforward; setting the older of the two people as "old", and the younger age as "young".
        old=max(age1,age2)
        young=min(age1,age2)
        #Counter to be returned.
        k=0
        #We set the iteration range so that the age of the elder of the two people does not exceed one hundred. We're
        #being pessimistic and assuming that the bloke's mum don't live past a hundred, see.
        for i in range(100-old):
            o=str(old+i)
            o=o.zfill(2)
            y=str(young+i)
            y=y.zfill(2)
            if o[::-1]==y:
                k+=1
    return k

def author_age(num):
    """This function returns a set of all possible non-zero age differences for the Car Talk Puzzler."""
    s=set()
    for i in range(100):
        #So we don't waste time double-counting, we want to set the range of the second iteration loop to exclude those
        #numbers that have been tested in the first loop.
        for j in range(100-i):
            #This check is essential; the bloke insists that he and his mum will have palindromic ages eight times.
            if check_age(i,j)==num:
                element=abs(i-j)
                #We want non-zero age differences for obvious reasons and we don't want duplicates.
                if element not in s and element!=0:
                    s.add(element)
    return s
    #There are two possible age differences for num = 8: nine and eighteen. We will go with the latter.

print(author_age(8))

def print_age(n):
    """This function prints the instances that two people n years apart in age have palindromic ages."""
    #We set the mum's age at the time of the kid's birth.
    mum=n
    #Kid's age zero at this point.
    kid=0
    while mum<=100:
        #We use the same palindromic check method as in the check_age function.
        o = str(mum)
        o = o.zfill(2)
        y = str(kid)
        y = y.zfill(2)
        #We want to know the palindromic ages of the bloke and his mum, hence the check and the command to print if it is true.
        if o[::-1] == y:
            print((kid,mum))
        mum+=1
        kid+=1
    #The guy was fifty-seven in 2015, which is the year this textbook was published, I think.
