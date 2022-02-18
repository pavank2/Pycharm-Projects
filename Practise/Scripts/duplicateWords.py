import collections

sentence="""As far as the laws of mathematics refer they reality they as not certain of anything"""

words = sentence.split()

words_counter = collections.Counter(words)

for word,count in sorted(words_counter.items()):
    if count > 1:
        print(word,count)

