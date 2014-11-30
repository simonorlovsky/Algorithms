def loadWords():
    words = []
    f = open("/Accounts/courses/cs111/dlibenno/data/twl98.txt")
    for line in f:
        words.append(line.strip())
    f.close()
    return words

def linearSearch(L,x):
    i = 0
    while i < len(L) and L[i] <= x:
        print L[i]
        if L[i] == x:
            return True
        i = i + 1
    return False

def binarySearch(L,x):
    left = 0
    right = len(L) - 1
    # We're absolutely sure that, if x in L, then x is one of 
    # L[left], L[left+1], ... L[right].
    while left <= right:
        middle = (left + right) / 2
        print L[middle], "is the middle of the range", left, right
        if L[middle] == x:
            return True
        elif L[middle] > x:
            left = left
            right = middle - 1
        else:  # that is, L[middle] < x
            left = middle + 1
            right = right
    return False
    


words = loadWords()
#linearSearch(words,"TMESIS")
#result = linearSearch(words,"SCHADENFREUDE")
#print "We", result, "ly found the word SCHADENFREUDE."
#linearSearch(words,"ZZZTOP")
#binarySearch(words,"TMESIS")
binarySearch(words,"PHILAFINDELPHIA")
