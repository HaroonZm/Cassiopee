from collections import Counter

N = input()
S = input().split('+')

dic_chr_num = Counter(S)
dic_num_kind = Counter(dic_chr_num.values())

ans = 4 * len(dic_chr_num) - 1
for num, kind in dic_num_kind.items():
    if num == 1:
        ans -= 2 * kind
    elif kind >= 2:
        ans -= 2 * (kind - 2)

print(ans)