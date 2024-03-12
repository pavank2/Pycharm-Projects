# Sort a given array of distinct integers where all its numbers are sorted except two numbers

def sort_one(a):
    # find which two numbers are out of place

    i = 0
    index1, index2 = -1, -1
    while i < len(a):
        if a[i] > a[i+1] and index1 != -1:
            index2 = i+1
            break
        elif a[i] > a[i+1] and index1 == -1:
            index1 = i
            i = i + 1
        else:
            i = i + 1

    print(f"Indexes to be swapped {index1} and {index2}")

    # Swap them

    a[index1],a[index2] = a[index2],a[index1]
    return (a)

a = [3,5,22,8,14,18,6]
print(f"Sorted array is {sort_one(a)}")