words = input().split()
counts = {}

for word in words:
    # J'essaie d'ajouter 1 si le mot est déjà dans le dict
    try:
        counts[word] += 1
    except KeyError:
        counts[word] = 1

# Mot le plus long
longest_word = max(words, key=len)

# Mot le plus fréquent, je suppose
most_common = max(counts.items(), key=lambda item: item[1])

print(most_common[0], longest_word)