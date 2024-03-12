    # Given an array of integers temperatures represents the daily temperatures,
    # return an array answer such that answer[i] is the number of days you have
    # to wait after the ith day to get a warmer temperature. If there is no future day
    # for which this is possible, keep answer[i] == 0 instead.

'''
def wait_days(a):
    i,j = 0,0
    wait = []
    while i < len(a) - 1:
        j = i + 1
        while j < len(a):
            if a[j] > a[i]:
                wait.append(j-i)

                break
            j += 1

            if j == len(a):
                wait.append(0)
        i += 1
    return wait
'''

# Using stack
def wait_days(a):

    n = len(a)
    result = [0]*n
    stack = []

    for i in range(n):
        while stack and a[i] > a[stack[-1]]:
            index = stack.pop()
            result[index] = i - index

        stack.append(i)

    return result

temp = [73,72,74,75,71,69,72,76,73]
print(wait_days(temp))