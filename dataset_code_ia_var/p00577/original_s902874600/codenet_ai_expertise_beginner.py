n = int(input())
s = input()

i = 0
ans = 0
while i + 1 < n:
    pair = s[i] + s[i+1]
    if pair == 'OX' or pair == 'XO':
        ans = ans + 1
        i = i + 2
    else:
        i = i + 1
print(ans)