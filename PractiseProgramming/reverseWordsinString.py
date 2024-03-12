#Reverse the words in a given string

def reverse_words(str):
    words = str.split()

    reversed = words[::-1]

    reversed_words = " ".join(reversed)
    return reversed_words



str = "I am on a train"
print(reverse_words(str))