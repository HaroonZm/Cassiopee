S = input()

items = ['A', 'G', 'C', 'T']
ans = 0
length = 0
for i in range(len(S)):
    if S[i] in items:
        length += 1
    else:
        ans = max(ans, length)
        length = 0
else:
    ans = max(ans, length)

print(ans)