# List the elements in the array which are duplicates

def duplicate_nums(a):
    count_ele = dict()
    for ele in a:
        count_ele[ele] = a.count(ele)

    for key in count_ele:
        if count_ele[key] > 1:
            print(key)

a = [2,3,1,2,3,100,100,200]
duplicate_nums(a)