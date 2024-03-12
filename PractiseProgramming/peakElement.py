# Find peak element in an array. A peak element is an element that is strictly greater than its neighbors.

def peak_element(a):
    i = 0
    while i < len(a):
        if a[i-1] < a[i] and a[i+1] < a[i]:
            print(a[i])
        i += 1

a = [1,2,3,1]
peak_element(a)