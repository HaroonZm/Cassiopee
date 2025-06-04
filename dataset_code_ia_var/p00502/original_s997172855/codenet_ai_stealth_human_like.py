d, n = map(int, input().split())
t = []
for _ in range(d):
    t.append(int(input()))
abc = []
for _ in range(n):
    abc.append(list(map(int, input().split())))

# ouais je fais un mémo ici, un peu la bourrin
memo = [-1 for _ in range(101)]

t_list = []
for _ in range(61):
    t_list.append(set())

for i in range(n):
    a, b, c = abc[i]
    for j in range(a, b+1):
        t_list[j].add(c)

# initialise les valeurs possibles pour le premier élément de t
for i in t_list[t[0]]:
    memo[i] = 0

# c'est moche mais ça fait le taf
for idx in range(1, len(t)):
    current_t = t[idx]
    new_memo = [-1]*101
    choices = list(t_list[current_t])
    for old in range(101):
        if memo[old] != -1:
            for ch in choices:
                # je suis pas sûr si max() est la meilleure idée ici mais bon
                new_memo[ch] = max(new_memo[ch], memo[old] + abs(old-ch))
    memo = new_memo

# print le résultat, j'espère qu'il y a toujours au moins un chemin
print(max(memo))