def solve():
    N, A, B = [int(x) for x in input().split()]
    S = input()
    a, b = 0, 0
    Ans = ['No'] * N
    for i in range(N):
        s = S[i]
        if s == 'c':
            continue
        if s == 'a':
            if a + b < A + B:
                Ans[i] = 'Yes'
                a += 1
        if s == 'b':
            if a + b < A + B and b < B:
                Ans[i] = 'Yes'
                b += 1
    for ans in Ans:
        print(ans)

if __name__ == "__main__":
    solve()