import random

def selectionSort(L):
    '''Repeatedly find the smallest element of L, and put it
       in the first unassigned position of L.'''
    for i in range(len(L)):
        print L
        smallestIndex = i
        for j in range(i+1,len(L)):
            if L[j] < L[smallestIndex]:
                smallestIndex = j
        L[i], L[smallestIndex] = L[smallestIndex], L[i]
    return L

def insertionSort(L):
    '''Repeatedly lengthen the sorted prefix of the list by one element.'''
    for i in range(len(L)-1):
        # Right now, L[0] ... L[i] is sorted.
        # Let's move the next element into place!
        j = i + 1
        while j > 0 and L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
            j = j - 1
    return L

def bubbleSort(L):
    '''Repeatedly walk through the list, swapping adjacent elements
       that are out of order.'''
    for i in range(len(L)):
        print L
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


def mergeSort(L):
    print "I'm sorting this list:", L
    if len(L) <= 1:
        return L
    else:
        left = mergeSort(L[0:len(L)/2])
        right = mergeSort(L[len(L)/2:])
        a = 0  # left[a] is the smallest unused element of left.
        b = 0  # right[b] is the smallest unused element of right.
        c = 0  # the smaller of left[a] and right[b] will go into L[c]
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                L[c] = left[a]
                a = a + 1
                c = c + 1
            else:
                L[c] = right[b]
                b = b + 1
                c = c + 1
        while a < len(left):
            L[c] = left[a]
            c = c + 1
            a = a + 1
        while b < len(right):
            L[c] = right[b]
            c = c + 1
            b = b + 1
        print "Now I've sorted this: ", L
        return L
        
       

#L = random.randint(0,100) for i in range(42)]
L = [12, 42, 23, 78, 94, 18, 39, 24, 64, 32]
#L = [99, 98, 97]
print L
#selectionSort(L)
#insertionSort(L)
#bubbleSort(L)
mergeSort(L)
print L
