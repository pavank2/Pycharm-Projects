#You are given a string s, which contains stars *.
#Choose a star in s.
#Remove the closest non-star character to its left, as well as remove the star itself.
#Return the string after all stars have been removed.

def remove_stars(s):
    stack = []

    for char in s:
        if stack and char == '*':  # If star is present. remove the top of the stack which is string to left
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)

s = "aa****a"
print(remove_stars(s))
# Output should be "lecoe"

