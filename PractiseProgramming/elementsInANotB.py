# Given two sorted arrays A & B, list elements in A but not in B

def aNotb(a,b):

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] in b:
            i += 1
            j += 1
        else:
            print(a[i])
            i += 1


a = [12,17,31,35,38,41,42,50, 65]
b = [17,19,23,31,40,42,43]
aNotb(a,b)