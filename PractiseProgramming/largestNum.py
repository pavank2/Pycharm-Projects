
# Largest num with the given number of digits and sum of digits

def largestNum(sum,num):
    largestNum = []
    while (sum > 9):
        largestNum.append("9")
        sum -= 9


    largestNum.append(sum)

    l = len(largestNum)

    while (l < num):
        largestNum.append("0")
        l += 1
    return ''.join(str(x) for x in largestNum)

N,S = 5,24
print(largestNum(S,N))