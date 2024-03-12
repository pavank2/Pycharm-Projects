# Count distinct elements in every window of size k

def distinct_window(a,k):
    i=0
    while i < len(a) - k + 1 :
       # Implementation with set
       # print(len(set(a[i:i+k])))
       # i += 1

       # Implementation with dict
       j = i
       count_distinct = 0
       count_nums = dict()
       for ele in a[i:i+k]:
            count_nums[ele] = count_nums.get(ele)

       print(len(count_nums))
       i += 1

a = [1,2,2,3,1,1,4]
k = 3
distinct_window(a,k)