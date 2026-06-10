import string
word_count={}
with open('poem.txt','r') as f:
    for line in f:
        line = line.lower().translate(
            str.maketrans('', '', string.punctuation)
        )
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word,0)+1

max_count = max(word_count.values())
for word,count in word_count.items():
    if count == max_count:
        print(word)
        print(f'the word {word} has {count} occurences')
