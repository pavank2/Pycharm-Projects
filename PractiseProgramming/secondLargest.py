
def second(a):
    if a[0] > a[1]:
        largest = a[0]
        sec = a[1]
    else:
        largest = a[1]
        sec = a[0]
    i=2
    while i < len(a):
        if a[i] > largest:
            sec = largest
            largest = a[i]

        elif a[i] > sec:
            sec = a[i]
        else:
            None
        i = i + 1
    return sec


a = [6, 2, 4, 20, 14, 42, 5]
print(second(a))