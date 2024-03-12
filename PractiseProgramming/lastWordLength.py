# Return the length of the last word in the string

def lastWordLen(s):
    s = s.strip()
    #slist = s.split() # Splits into words
    # print(len(slist[-1]))

    #Another way
    lastWord = s[s.find(' ')+1:]
    print(len(lastWord))

s = "Hello World"
lastWordLen(s)