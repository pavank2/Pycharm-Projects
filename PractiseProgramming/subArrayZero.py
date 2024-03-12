
def zero_subarray(a):
    sums = dict()
    curr_sum = 0
    i = 0
    while i < len(a):
        curr_sum += a[i]

        for key,value in sums.items():
            if value == curr_sum:
                print(key+1,i)
                break

        sums[i] = curr_sum
        i += 1

a = [4, 8,2, -3, 1, 6]
zero_subarray(a)