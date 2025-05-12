# Solved by QBnewb
# Discretization
# off-line

q = int(input())
s = []
rs = [] # for discretization

# download the input
for i in range(q):
    s.append(input().split())
    if s[i][0] == '3':
        rs.append(s[i][1])
        rs.append(s[i][2])
    else:
        rs.append(s[i][1])

rs = sorted(list(set(rs)))
index = {rs[i]:i for i in range(len(rs))} # discretization
d = [[] for i in range(len(rs))] # discrete dictionary
for i in range(q):
    op, key = int(s[i][0]), s[i][1]
    idx = index[key]
    if op == 0:
        d[idx].append(s[i][2])
    elif op == 1:
        for item in d[idx]:
            print(item)
    elif op == 2:
        d[idx].clear()
    else:
        l = idx
        r = index[s[i][2]]
        for j in range(l, r+1):
            for item in d[j]:
                print(rs[j], item)