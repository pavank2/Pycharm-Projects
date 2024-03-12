# Find the intersection of two sorted arrays

def intersection(a1,a2):

    inter = []
    i=0
    j=0

    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            inter.append(a1[i])
            i = i + 1
            j = j + 1
        elif a1[i] < a2[j]:
            i = i + 1
        else:
            j = j + 1
    return inter


arr1 = [1,2,5, 8, 10, 16, 24, 43, 72]
arr2 = [2,5,9,23,43]

print(intersection(arr1,arr2))