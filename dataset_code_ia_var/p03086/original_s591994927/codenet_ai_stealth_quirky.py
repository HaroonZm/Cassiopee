S = input()
chars = {'A', 'C', 'G', 'T'}

longest = 0
spot = 0
while spot < len(S):
    if S[spot] not in chars:
        spot += 1
        continue
    p = spot
    while p < len(S) and S[p] in chars:
        p += 1
    if (p - spot) > longest:
        longest = p - spot
    spot = p + 1 if p == spot else p

print(longest)