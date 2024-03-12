# Find the longest substring without repeating characters in a given string

def longest_substr(str):
    start_index = 0
    max_len = 0
    curr_len = 0
    char_index_map = {}

    for i,char in enumerate(str):  # enumerate returns a list [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]
        if char in char_index_map and char_index_map[char] >= start_index: # If a char is repeating
            start_index = char_index_map[char] + 1  # Skip that char and slide the starting point

        char_index_map[char] = i
        curr_len = i - start_index + 1

        if curr_len > max_len:
            max_len = curr_len

    return str[start_index: start_index + max_len]


s = "abbcacbbc"
print(longest_substr(s))

14, 9, 11, 14, 6, 12, 3