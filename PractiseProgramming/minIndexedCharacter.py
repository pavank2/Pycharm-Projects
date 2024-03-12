#Given a string str and another string patt.
#Find the character in patt that is present at the minimum index in S.

def min_index(str,patt):
    min_index = -1
    for char in patt:
        if char in str:
            if min_index == -1 or min_index > str.index(char):
                min_index = str.index(char)

    print(min_index)
str = "szffsyle"
patt = "bfherjz"
min_index(str,patt)