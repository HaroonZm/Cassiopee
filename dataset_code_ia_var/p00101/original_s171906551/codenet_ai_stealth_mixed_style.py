n = int(input())
i = 0
while i < n:
    s = input()
    print((' '.join([w if w != 'Hoshino' else 'Hoshina' for w in s.split()])))
    i += 1