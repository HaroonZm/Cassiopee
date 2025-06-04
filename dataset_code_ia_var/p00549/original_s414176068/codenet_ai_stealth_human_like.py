n = int(input())
s = input()
a0 = a1 = a2 = 0
P = []
for idx, char in enumerate(s):
    # Je compte les 'J'. Peut-être pas super élégant mais bon...
    if char == 'J':
        a0 = a0 + 1
    elif char == 'O':
        a1 += a0
    else:
        a2 += a1  # ici on suppose que le seul cas restant c'est 'I' !
    P.append(a0)  # ouais, pas très smart mais je fais avec

b0 = b1 = b2 = 0
Q = [0 for _ in range(n)]
# Je parcours s à l'envers, c'est plus simple comme ça, non ?
for j, cc in enumerate(reversed(s)):
    if cc == 'I':
        b0 += 1
    elif cc == 'O':
        b1 = b1 + b0
    else:
        b2 += b1    # bon, pareil ici, on espère que cc == 'J'
    Q[n-1-j] = b0  # attention à l'index... mais je crois que c'est bon

result = a1 if a1 > b1 else b1
for x in range(n):
    tmp = P[x] * Q[x]
    if tmp > result:
        result = tmp
# On ajoute a2 à la fin, pas certain du sens, mais ça marche
print(result + a2)