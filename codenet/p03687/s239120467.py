from collections import Counter

s = input()

def convert(st, toS, cou):
    if st.count(st[0]) == len(st):
        return cou
    for i in range(len(st)):
        if i+1 < len(st) and st[i+1] == toS:
            st[i] = toS
    return convert(st[:-1], toS, cou+1)

ans = 200
for j in set(s):
    ans = min(ans, convert(list(s), j, 0))
print(ans)