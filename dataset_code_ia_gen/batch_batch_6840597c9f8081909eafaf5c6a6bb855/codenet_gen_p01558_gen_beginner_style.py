n, m = map(int, input().split())
s = input()

l = [1]
r = [1]

for _ in range(m):
    q = input()
    if q == "L++":
        l.append(l[-1] + 1)
        r.append(r[-1])
    elif q == "L--":
        l.append(l[-1] - 1)
        r.append(r[-1])
    elif q == "R++":
        l.append(l[-1])
        r.append(r[-1] + 1)
    else:  # R--
        l.append(l[-1])
        r.append(r[-1] - 1)

substrings = set()
for i in range(1, m+1):
    substr = s[l[i]-1:r[i]]
    substrings.add(substr)

print(len(substrings))