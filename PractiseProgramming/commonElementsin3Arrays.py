# Find common elements in 3 arrays

def common(a1,a2,a3):
    common_list = []
    for i in a1:
        try:
            index_in_arr2 = a2.index(i)
            index_in_arr3 = a2.index(i)
            common_list.append(i)

            a2.pop(index_in_arr2)
            a3.pop(index_in_arr3)  # To avoid duplicates
        except ValueError:
            continue

    return common_list



a1 = [2,4,6,8,12,14,16]
a2 = [4,8,10,12]
a3 = [8,10,10,12,14]

print(common(a1,a2,a3))
