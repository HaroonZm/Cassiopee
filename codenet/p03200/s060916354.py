S = input()
s = list(S)
l_s = len(s)
ans = 0
black_index = 0
for i in range(1, l_s)[::-1]:
    if s[i] == 'B':
        black_index += 1
        continue

    if s[i-1] == 'B':
        ans += l_s - i - black_index
        s[i] = 'B'
        s[i-1] = 'W'
        black_index += 1
print(ans)