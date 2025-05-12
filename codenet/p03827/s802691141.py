n = int(input())
s = input()
x = 0
ans = 0

for i in range(n):
    if s[i] == 'I':
        x += 1
        if ans < x:
            ans = x
    else:
        x -= 1

print(ans)