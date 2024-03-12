
original = input("Enter a sentence").strip().lower()


words =   original.split()
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_words.append(word + "yay")
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos+1
            else:
                 break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        changed_word = rest + cons + "ay"
        new_words.append(changed_word)

new_sentence = " ".join(new_words)
print(new_sentence)










