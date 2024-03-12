# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def find_substr(s2,s1):   # Find s2 in s1

    n = len(s1)
    m = len(s2)

    if (m > n):
        print("No needle in haystack")
        return -1

    for i in range(n - m + 1):
        if s1[i:i+m] == s2:
            return i


needle = "bac"
haystack = "acbadhhbacwef"

print(find_substr(needle,haystack))