# それぞれ辞書順に並び替えたものをとっていく
# 辞書にしたうちの最小値をとっていくことでN^3くらいでいけそう
n = int(input())
alphabets = [chr(i) for i in range(97, 97 + 26)]
maps = []
for _ in range(n):
    s = input()
    new_map = dict(zip(alphabets, [0 for _ in range(26)]))
    for si in s:
        new_map[si] += 1
    maps.append(new_map)

ans_map = dict(zip(alphabets, [10**9 for _ in range(26)]))
for m in maps:
    for k, v in m.items():
        ans_map[k] = min(ans_map[k], v)

ans = ""
for k in list(sorted(ans_map.keys())):
    ans += k * ans_map[k]
print(ans)