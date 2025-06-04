s = input()
b = s[0]
ans = 0
for i in s:
    if b != i:
        ans = ans + 1
    b = i
print(ans)