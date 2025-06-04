digits = list(map(int, input().split()))
A, B, C, D, E = digits

def split_time(val):
    return (val // 60, val % 60) if val >= 60 else (0, val)

X, Y = split_time(E)

C -= X ; D -= Y

def to_minutes(h, m): return h*60 + m

print(to_minutes(C, D) - to_minutes(A, B))