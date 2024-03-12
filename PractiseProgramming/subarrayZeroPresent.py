# Check if a given array contains a subarray with 0 sum

def check_subarray(a):
    sum_set = set()

    cumu_sum = 0

    for num in a:
        cumu_sum += num

        if cumu_sum in sum_set or cumu_sum == 0: # if cumulative sum repeats with an already stored cumulative sum in sum_set
            return "Subarray with zero sum is present"

        sum_set.add(cumu_sum)  # Or add this cumu_sum to existing sums

    return "Subarray with zero sum is not present"

a = [4, 2, -3, 1, 6]
print(check_subarray(a))