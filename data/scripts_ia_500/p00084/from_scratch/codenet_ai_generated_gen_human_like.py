sentence = input().strip()
for ch in ['.', ',', ' ']:
    sentence = sentence.replace(ch, ' ')
words = sentence.split()
filtered_words = [w for w in words if 3 <= len(w) <= 6]
print(' '.join(filtered_words))