N = int(input())
S1 = input()
S2 = input()

domino = []
i = 0
while i < N:
    if S1[i] == S2[i]:
        domino.append(1)
        i += 1
    else:
        domino.append(0)
        i += 2

if domino[0] == 1:
    result = 3
else:
    result = 6

for j in range(1, len(domino)):
    if domino[j] == 1:
        if domino[j-1] == 1:
            result = result * 2
    else:
        if domino[j-1] == 1:
            result = result * 2
        else:
            result = result * 3

print(result % 1000000007)