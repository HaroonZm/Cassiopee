from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

# Vérification de l'unicité via Counter
if max(Counter(words).values(), default=0) > 1:
    print("No")
elif any(a[-1] != b[0] for a, b in zip(words, words[1:])):
    print("No")
else:
    print("Yes")