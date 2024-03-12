# Two strings s and t are isomorphic if the characters in s can be replaced to get t
# Input: s = "egg", t = "add"
# Output: true

def isomorphic(s,t):
    char_map = dict()

    i = 0
    while i < len(s):
        if char_map.get(s[i]) and char_map[s[i]] != t[i]:
            return False

        char_map[s[i]] = t[i]
        i += 1

    return True
s = "egg"
t = "add"
print(isomorphic(s,t))

s = "cbacdcbcacd"
print(s.find("acd")) # First position where it was found
print(s.rfind("acd")) # Last position




