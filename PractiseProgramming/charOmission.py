#program that returns the missing letter from an array of increasing letters (upper or lower).
# Assume there will always be one omission from the array.

def missing_char(a):

    i=0
    while i < len(a):
        if ord(a[i])+ 1 != ord(a[i+1]):
            return chr(ord(a[i])+ 1)


a = ['p', 'r', 's','t']
print(f"Missing char is {missing_char(a)}")
