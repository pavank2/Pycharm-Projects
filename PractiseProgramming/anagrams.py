# Verify if two strings are anagrams

def are_anagrams(s1,s2):

    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    return sorted(s1) == sorted(s2)


s1 = "Hello"
s2 = "eloHi"
if are_anagrams(s1,s2):
    print(f"{s1} and {s2} are anagrams")
else:
    print(f"{s1} and {s2} are not anagrams")