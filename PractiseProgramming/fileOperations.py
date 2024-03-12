# Count the number of characters, words, lines in a file

def file_operations(f):

    words = []
    try:
        with open(f,'r', encoding='utf-8') as file:
            count_words = dict()
            content = file.read()

            chars = len(content)

            words = content.split()

            lines = len(content.split('\n'))

            print (f"file stats: {chars},{len(words)},{lines}")

        # Find max repeated word
        for word in words:
            count_words[word] = words.count(word)

        max_count = 0

        for word in words:
            if count_words[word] > max_count:
                max_count = count_words[word]
                max_word = word

        print(f"Maximum occurring word is \"{max_word}\" and occurs {max_count} times")
    except FileNotFoundError:
        print("File not found")

filepath = 'example.txt'

file_operations(filepath)

