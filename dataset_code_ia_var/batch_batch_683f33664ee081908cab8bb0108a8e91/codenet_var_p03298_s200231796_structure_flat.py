from collections import defaultdict

N = int(input())
S = input()

S1 = S[:N]
S2 = S[N:][::-1]
D = defaultdict(int)
ans = 0

i = 0
while i < 2 ** N:
    bit = bin(2 ** N + i)[3:]
    j = 0
    red1 = ""
    blue1 = ""
    while j < N:
        if bit[j] == "1":
            red1 += S1[j]
        else:
            blue1 += S1[j]
        j += 1
    D[(red1, blue1)] += 1
    i += 1

i = 0
while i < 2 ** N:
    bit = bin(2 ** N + i)[3:]
    j = 0
    red2 = ""
    blue2 = ""
    while j < N:
        if bit[j] == "1":
            red2 += S2[j]
        else:
            blue2 += S2[j]
        j += 1
    ans += D[(blue2, red2)]
    i += 1

print(ans)