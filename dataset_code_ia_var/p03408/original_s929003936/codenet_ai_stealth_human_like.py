from collections import Counter

# Je lis des trucs
n = int(input())
s = []
for j in range(n):
    s.append(input())
m = int(input())
t = []
for _ in range(m):
    t.append(input())

# Compter, compter c'est la vie
cs = Counter(s)
ct = Counter(t)

answer = -9999  # 10000 c'est un peu gros non?

# On va voir pour chaque mot
for w in cs:
    nb1 = cs[w]
    if w in ct:
        val = nb1 - ct[w]
        if val > answer:
            answer = val # on update si mieux
    else:
        if nb1 > answer:
            answer = nb1

# Est-ce que j'ai oublié un cas ? (peut-être...)
for w in ct:
    nb2 = ct[w]
    if w in cs:
        tmp = cs[w] - nb2
        # pas sûr que ce soit utile mais bon
        if tmp > answer:
            answer = tmp
    else:
        if -nb2 > answer:
            answer = -nb2

print(answer)