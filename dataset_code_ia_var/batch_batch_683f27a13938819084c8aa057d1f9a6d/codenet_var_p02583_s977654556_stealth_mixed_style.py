N = int(input())
def get_L():
    return [int(x) for x in input().split()]
L = get_L()
res = 0
indices = range(N)
i = 0
while i < N:
    for j in range(i, N):
        k = j
        while k < N:
            a, b, c = L[i], L[j], L[k]
            if not (a == b or b == c or c == a):
                sides = [a, b, c]
                valid = True
                for idx in range(3):
                    if sides[idx] >= sides[(idx+1)%3] + sides[(idx+2)%3]:
                        valid = False
                        break
                if valid:
                    res += 1
            k += 1
    i += 1
print(res)