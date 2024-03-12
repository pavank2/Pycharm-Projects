# Compress a string of chars eg. chars = ["a","a","b","b","c","c","c"] becomes "a2b2c3"

def compress_string(chars):
    char_count = 1
    i = 0
    compressed_str = []
    l = len(chars)
    while i < l - 1:
        if chars[i] != chars[i+1]:
            compressed_str.append(chars[i])
            compressed_str.append(char_count)
            char_count = 1
        else:
            char_count += 1

        i += 1
    compressed_str.append(chars[l - 1])
    compressed_str.append(char_count)
    print (compressed_str)

chars = ["a","a","b","b","c","c","c","d","e"]
compress_string(chars)