# Given a string s, return the longest palindromic substring in s
def longestPal(s):

    i = 0
    max_len = 0
    curr_len = 0


    while i  < len(s):
        j = i
        while j < len(s):

            if s[i:j] == ''.join(reversed(s[i:j])):

                curr_len = j - i
                if curr_len > max_len:
                    max_len = curr_len
                    start = i
                    end = j
            j += 1
        i += 1

    print(max_len,start,end)
s = "babad"
longestPal(s)