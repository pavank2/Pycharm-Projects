# Reverse a string while Preserving spaces in a string
# NOT WORKING AS EXPECTED
def reverse_string_with_spaces(input_str):
    # Split the string into a list of characters
    char_list = list(input_str)

    # Identify the positions of spaces in the original string
    space_positions = []
    for i, char in enumerate(char_list):
        if char.isspace():
            space_positions.append(i)

    # Reverse the non-space characters
    non_space_chars = []
    for char in char_list:
        if not char.isspace():
            non_space_chars.append(char)
    non_space_chars.reverse()
    print(non_space_chars)

    # Insert the reversed non-space characters back into the original positions
    for i, char in zip(space_positions, non_space_chars):
        char_list[i] = char

    # Convert the list back to a string
    reversed_str = ''.join(char_list)

    return reversed_str

# Example usage:
input_string = "Hello World! Python is great"
result = reverse_string_with_spaces(input_string)
print(result)