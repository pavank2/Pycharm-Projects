# Continuous sub array of the given array whose sum is equal to a given number
def contSubArray(a,target):

    i= 0
    sum = 0
    startindex = 0
    while i < len(a):
        sum += a[i]

        while (sum > target):
            sum -= a[startindex]
            startindex += 1

        if (sum == target):
            print(f"Subarray {a[startindex:i+1]}")
            return
        i += 1

a=[12,30, 10, 31, 14, 21, 8]
target = 45
contSubArray(a,target)
