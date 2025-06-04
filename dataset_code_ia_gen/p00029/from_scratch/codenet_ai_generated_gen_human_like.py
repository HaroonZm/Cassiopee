text = input().strip()
words = text.split()

# Calculer la fréquence des mots
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Trouver le mot le plus fréquent
most_freq_word = max(freq, key=freq.get)

# Trouver le mot avec le maximum de lettres
longest_word = max(words, key=len)

print(most_freq_word, longest_word)