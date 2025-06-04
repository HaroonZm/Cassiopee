L = [int(i) for i in input().split()]
has_even = False
for l in L:
    if l % 2 == 0:
        has_even = True
        break
if has_even:
    print(0)
else:
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
    print(L[0] * L[1])