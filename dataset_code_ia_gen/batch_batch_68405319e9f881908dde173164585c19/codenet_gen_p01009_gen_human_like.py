import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, Q = map(int, input().split())

# parent[i]: parent of i in union-find tree
# diff[i]: (parent[i]'s strength) - (i's strength)
parent = [i for i in range(N+1)]
diff = [0]*(N+1)

def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        diff[x] += diff[parent[x]]
        parent[x] = p
        return parent[x]

def unite(a, b, c):
    # (strength_b) - (strength_a) = c
    # i.e. strength_b = strength_a + c
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    # Let's attach ra under rb
    # diff[x]: strength_parent[x] - strength_x
    # We want to set parent[ra] = rb, and update diff[ra]
    # Since diff[x] stores parent strength - x, after union,
    # diff[ra] = (strength_rb) - (strength_ra)
    # From known values:
    # diff[a]: strength_parent[a] - strength_a
    # diff[b]: strength_parent[b] - strength_b
    # We have:
    # strength_b - strength_a = c
    # But:
    # strength_a = strength_ra - diff[a]
    # strength_b = strength_rb - diff[b]
    # Thus:
    # (strength_rb - diff[b]) - (strength_ra - diff[a]) = c
    # strength_rb - strength_ra = c + diff[b] - diff[a]
    # So:
    diff_ra = c + diff[b] - diff[a]
    parent[ra] = rb
    diff[ra] = diff_ra

def diff_strength(a, b):
    # if connected, return (strength_b - strength_a)
    # else None
    ra = find(a)
    rb = find(b)
    if ra != rb:
        return None
    # strength_a = strength_ra - diff[a]
    # strength_b = strength_rb - diff[b]
    # Since ra==rb, strength_ra == strength_rb
    # So difference = strength_b - strength_a = (strength_rb - diff[b]) - (strength_ra - diff[a]) = diff[a] - diff[b]
    # Note: diff[x] = strength_parent[x] - strength_x
    return diff[a] - diff[b]

for _ in range(Q):
    query = input().split()
    if query[0] == "IN":
        _, A, B, C = query
        A = int(A)
        B = int(B)
        C = int(C)
        unite(A, B, C)
    else:  # COMPARE
        _, A, B = query
        A = int(A)
        B = int(B)
        res = diff_strength(A, B)
        if res is None:
            print("WARNING")
        else:
            print(res)