# Merge two sorted arrays

def merge_array(a,b):
    c = []

    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
        k += 1

    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1


    return c

a = [2,40,42]
b = [6,11,14,38]
print(merge_array(a,b))