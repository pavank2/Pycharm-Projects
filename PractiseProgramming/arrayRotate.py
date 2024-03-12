
#Rotate array left by 2 places
def rotate_array(arr,d):
    l = len(arr)
    tempArr = []

    i = 0
    j=0
    while i < d:
        tempArr.append(arr[i])
        i=i+1

    i=d
    while  i < l:
        arr[i-d] = arr[i]
        i = i+1

    i = 0
    j = d
    while i < d:
        arr[l-j+1] = tempArr[i]
        i = i + 1
        j = j + 1

    return arr

# Another technique
# Reverse the elements from the start to k-1.
# Reverse the elements from k to the end.
# Reverse the entire array.
arr = [1,2,3,4,5]
d = 2



print(list(reversed(arr[:2])))
print(rotate_array(arr,d))
