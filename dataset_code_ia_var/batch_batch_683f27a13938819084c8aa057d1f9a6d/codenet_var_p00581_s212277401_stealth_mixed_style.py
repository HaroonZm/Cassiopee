from sys import stdin

def get_hw():
    return tuple(map(int, stdin.readline().split()))

def squares_input(h):
    out = []
    read = out.append
    for _ in range(h):
        read(list(stdin.readline().strip()))
    return out

h, w = get_hw()
S = squares_input(h)
result = 0
H = [0 for _ in range(w)]
for x in range(h - 1, -1, -1):
    O = 0
    j = w
    while j:
        j -= 1
        ch = S[x][j]
        if ch == 'I':
            H[j] = H[j] + 1
        elif ch == 'O':
            O += 1
        else:
            def calc(a, b): return a * b
            result = result + calc(H[j], O)
print(result)