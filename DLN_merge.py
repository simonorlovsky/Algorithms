def merge(A,B):
    L = []
    a = 0  # A[a] is the smallest unused element of A.
    b = 0  # B[b] is the smallest unused element of B.
    while a < len(A) or b < len(B):
        print "merge: let's see if this works:", a, b
        if a < len(A) and (b >= len(B) or A[a] < B[b]):
            L.append(A[a])
            a = a + 1
        else:
            L.append(B[b])
            b = b + 1
    return L

def merge(A,B):
    if len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    elif A[0] < B[0]:
        return [A[0]] + merge(A[1:],B)
    else:
        return [B[0]] + merge(A,B[1:])

def mergeSort(L):
    if len(L) <= 1:
        return L
    else:
        left = mergeSort(L[0:len(L)/2])
        right = mergeSort(L[len(L)/2:])
        print "MS:", left, right
        return merge(left,right)

sample = [521, 111, 101, 672, 20, 16, 0, 3, 8000, 8001]
result = mergeSort(sample)
print "main:", result
