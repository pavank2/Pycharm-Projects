# First Repeating character in a string
def firstRepeat(str):
    count_chars = dict()
    for char in str:
        count_chars[char] = str.count(char)

    for char in str:
        if count_chars[char] > 1:
            return char


str = "This is a string"
print(firstRepeat(str))
