
# Not correct
def longestSub(str1,str2):
    longest = 0
    prev_index = -1
    for char in str1:
        if char in str2:
                longest += 1
                print(char)

    print(longest)

s1 = "ABCDGH"
s2 = "AEDFHR"

longestSub(s1,s2)