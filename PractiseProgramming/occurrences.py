# Print number of occurrences of each number in the list

def occurences(arr):
    occ = dict()
    for num in arr:
        occ[num] = arr.count(num)
    #Sort by keys
    return dict(sorted(occ.items()))
    #Sort by values
    #return dict(sorted(occ.items(), key=lambda item: item[1]))


arr = [2 ,1, 4, 7,3, 2, 4, 9,4, 3]
print(occurences(arr))
