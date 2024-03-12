# Move all 0's to the end of an array. Maintain the relative order of the other (non-zero) array elements.

def move_zeros(a):
    temp_arr = [-1]*len(a)
    i=0
    j=len(a)-1
    k=0
    for num in a:
        if num == 0:
            temp_arr[j]=0
            j=j-1
        else:
            temp_arr[k] = num
            k=k+1

    return temp_arr

a = [0,4,0,1,6,8,3]
print(move_zeros(a))