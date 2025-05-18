def main():
    _ = int(input())
    A = list(map(int, input().split()))

    A.append(-1)
    A = [a for a, b in zip(A, A[1:]) if a != b]
    A.insert(0, -1)
    A.append(-1)
    A = [b for a, b, c in zip(A, A[1:], A[2:]) if (a < b) != (b < c)]

    A.append(-1)
    A = sorted((a, (1 if a < b else -1)) for a, b in zip(A, A[1:]))

    n = 1
    n_max = 0
    prev = 0
    for a, s in A:
        if prev < a:
            if n_max < n:
                n_max = n
            prev = a
        n += s
    print(n_max)
main()