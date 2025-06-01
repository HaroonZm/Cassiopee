n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)

parent = []
club = []
for i in range(n):
    parent.append(i)
    club.append(-1)

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

for count in range(1, k+1):
    line = input().split()
    t = int(line[0])
    a = int(line[1]) - 1
    b = int(line[2]) - 1

    if t == 1:
        p_a = find(a)
        p_b = find(b)
        c_a = club[p_a]
        c_b = club[p_b]

        if c_a != -1 and c_b != -1 and c_a != c_b:
            print(count)
            break

        if c_a == -1 and c_b != -1:
            club[p_a] = c_b

        parent[p_b] = p_a

    else:
        p_a = find(a)
        if club[p_a] == -1:
            club[p_a] = b
        elif club[p_a] != b:
            print(count)
            break
else:
    print(0)