# Print Contiguous SubArray With Maximum Sum

def contSubArray_maxSum(a):

    curr_sum = 0
    max_sum = 0
    i = 0
    start = 0
    end = 0
    while i < len(a):
        curr_sum += a[i]

        if curr_sum < 0:     # If sum becomes less than 0, discard the sum and start with next index with sum 0
            curr_sum = 0
            start = i + 1
        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i
        i += 1

    print(a[start:end+1])




a = [2, -3, 7, -4, 2, 5, -8, 6, -1]
contSubArray_maxSum(a)