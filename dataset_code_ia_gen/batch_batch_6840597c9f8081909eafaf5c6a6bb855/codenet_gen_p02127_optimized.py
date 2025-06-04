import sys
sys.setrecursionlimit(10**7)

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

n = len(s)
m = len(t)

# Pré-calcul des prochaines positions pour chaque caractère de t dans s, pour accélérer la recherche de sous-séquences
# next_pos[i][c] = la plus petite position >= i dans s où se trouve le caractère c, sinon -1
next_pos = [[-1] * 52 for _ in range(n + 1)]

def char_to_index(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a')
    else:
        return ord(c) - ord('A') + 26

for c in range(52):
    next_pos[n][c] = -1

for i in range(n - 1, -1, -1):
    for c in range(52):
        next_pos[i][c] = next_pos[i + 1][c]
    next_pos[i][char_to_index(s[i])] = i

A = [s]
count = 0

while True:
    B = []
    progressed = False
    for u in A:
        length = len(u)
        # Pour u, pré-calculer next_pos_u similaire pour accélérer la recherche du t comme sous-suite de u
        nextu = [[-1] * 52 for _ in range(length + 1)]
        for c in range(52):
            nextu[length][c] = -1
        for i in range(length - 1, -1, -1):
            for c in range(52):
                nextu[i][c] = nextu[i + 1][c]
            nextu[i][char_to_index(u[i])] = i

        # Chercher la première occurrence de t comme sous-suite dans u
        idx = 0
        pos_list = []
        for ch in t:
            cidx = char_to_index(ch)
            idx = nextu[idx][cidx]
            if idx == -1:
                break
            pos_list.append(idx)
            idx += 1
        else:
            # On peut découper u selon pos_list
            progressed = True
            parts = []
            prev = 0
            for p in pos_list:
                parts.append(u[prev:p])
                prev = p + 1
            parts.append(u[prev:])
            B.extend(parts)
            continue
        # Pas possible de découper u selon t, on garde u tel quel
        B.append(u)

    if not progressed:
        break
    A = B
    count += 1

print(count)