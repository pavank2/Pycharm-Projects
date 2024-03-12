#Sort an array of 0,1

def sort_array(a):
    i=0
    j = len(a) - 1

    while i < j and i < len(a) and j > 0:
        if a[i] == 0 and a[j] == 1:
            i += 1
            j -= 1
        elif a[i] == 1 and a[j] == 0:
           a[i], a[j] =  a[j], a[i]
           i += 1
           j -= 1

        elif a[i] == 1 and a[j] == 1:
            j -= 1

        else:
            i += 1

    return a

a = [1,1,1,1,0,0,0,0]
print(sort_array(a))

