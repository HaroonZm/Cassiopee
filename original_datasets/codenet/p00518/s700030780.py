def plus(s):
    global c
    d = [0] * 7
    for i in range(7):
        if s in g[i]:
            for j in range(7):
                if g[i] & g[j] != set():
                    d[i] += c[j]
    c = d

n = int(input())
s = input()
g = [set(["J"]), set(["O"]), set(["I"]), set(["J", "O"]), set(["J", "I"]), set(["O", "I"]), set(["J", "O", "I"])]
c = [1, 0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    plus(s[i])

print(sum(c) % 10007)