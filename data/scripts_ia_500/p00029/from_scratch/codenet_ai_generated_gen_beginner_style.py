text = input()
words = text.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_freq = 0
most_frequent_word = ""
for word in freq:
    if freq[word] > max_freq:
        max_freq = freq[word]
        most_frequent_word = word

max_length = 0
longest_word = ""
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print(most_frequent_word, longest_word)