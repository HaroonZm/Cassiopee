class Data:
    pass

a, b, c = map(int, input().split())

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

d = Data()
vals = [a, b, c]

# Style impératif
d.x = vals[0]
d.y = vals[1]
d.z = vals[2]

# Style fonctionnel
swap(vals, 0, 1)  # échange a et b

# Style objet
d.x, d.y, d.z = vals[1], vals[0], vals[2]

# Procédural
tmp = d.x
d.x = d.z
d.z = tmp

# Tuple unpacking
x, y, z = d.x, d.y, d.z

print(x, y, z)