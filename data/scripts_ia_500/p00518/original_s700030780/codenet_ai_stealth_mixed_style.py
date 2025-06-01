def plus(s):
    global c
    d = list(map(lambda x:0, range(7)))
    i = 0
    while i < 7:
        if s in g[i]:
            for j in range(7):
                if g[i].intersection(g[j]):
                    d[i] = d[i] + c[j]
        i += 1
    c[:] = d

n = int(input())
s = input()
g = [set(["J"]), set(["O"]), set(["I"]), {"J", "O"}, {"J", "I"}, {"O", "I"}, {"J", "O", "I"}]
c = [1]+[0]*7
for i in range(n):
    plus(s[i])

print((lambda x: x % 10007)(sum(c)))