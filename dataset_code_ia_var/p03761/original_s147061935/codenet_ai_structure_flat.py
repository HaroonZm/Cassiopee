n = int(input())
alphabets = [chr(i) for i in range(97, 123)]
maps = []
for _ in range(n):
    s = input()
    d = {}
    for a in alphabets:
        d[a] = 0
    for c in s:
        d[c] += 1
    maps.append(d)
ans_map = {}
for a in alphabets:
    ans_map[a] = 10**9
for i in range(n):
    m = maps[i]
    for a in alphabets:
        ans_map[a] = min(ans_map[a], m[a])
ans = ""
sorted_keys = sorted(alphabets)
for k in sorted_keys:
    ans += k * ans_map[k]
print(ans)