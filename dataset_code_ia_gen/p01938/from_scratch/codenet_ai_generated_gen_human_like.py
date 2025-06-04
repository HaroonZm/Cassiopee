S = input().strip()

# Tableau des lettres de A à Z en cercle
letters = [chr(ord('A') + i) for i in range(26)]

# Position initiale : 'A'
pos = 0
count = 0

for c in S:
    target = ord(c) - ord('A')
    steps = (target - pos) % 26
    # On avance étape par étape pour compter les passages sur 'A'
    for _ in range(steps):
        pos = (pos + 1) % 26
        if pos == 0:
            count += 1

print(count)