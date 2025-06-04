M = int(input())
for _ in range(M):
    A = int(input())
    Y = int(input())
    N = int(input())
    max_ = 0
    for _ in range(N):
        t, nenri, tax = map(float, input().split())
        if t == 0:
            w = 0
            a = A
            for _ in range(Y):
                w += int(a * nenri)
                a -= tax
            result = a + w
        else:
            a = A
            for _ in range(Y):
                a += int(a * nenri) - tax
            result = a
        max_ = max(max_, result)
    print(int(max_))