s = input().rstrip()
char_count = {}
for c in s:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1

total = len(s)
ans = 0

for c in s:
    char_count[c] -= 1
    total -= 1
    ans += total - char_count[c]
print(ans + 1)