# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place

def removeElement(a,val):
    i = 0 # array index
    j= 0 # val index
    count = 0

    while i < len(a):
        if a[i] == val:
            count += 1
        i += 1
    i= 0
    while i < len(a):
        if a[i] == val:
            i += 1
        else:
            a[j] = a[i]
            j += 1
            i += 1

    i = len(a) - 1

    while i > len(a) - count - 1:
        a[i] = '_'
        i -= 1
    return a

nums = [0,1,2,2,3,2,2,4,8]
val = 2
print(removeElement(nums,val))