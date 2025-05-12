n = int(input())
la = [int(w) for w in input().split()]

ans = 0
h = la[0]

for a in la[1:]:
    if a <= h:
        ans += h-a
    else:
        h = a

print(ans)