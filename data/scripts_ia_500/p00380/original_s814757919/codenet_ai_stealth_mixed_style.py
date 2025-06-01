def solve():
    N = int(input())
    a = list(map(int, input().split()))
    Q = int(input())
    sort_a = sorted(a)
    mismatch_count = sum(1 for i, val in enumerate(a) if val != sort_a[i])
    if mismatch_count == 0:
        print(0)
        return
    i = 0
    while i < Q:
        x, y = map(int, input().split())
        a[x-1], a[y-1] = a[y-1], a[x-1]
        def update_judge(judge, idx1, idx2):
            if a[idx1] == sort_a[idx1] and a[idx2] != sort_a[idx1]:
                return judge - 1
            if a[idx1] != sort_a[idx1] and a[idx2] == sort_a[idx1]:
                return judge + 1
            return judge
        mismatch_count = update_judge(mismatch_count, x-1, y-1)
        mismatch_count = update_judge(mismatch_count, y-1, x-1)
        if mismatch_count == 0:
            print(i + 1)
            break
        i += 1
    else:
        print(-1)

if __name__ == "__main__":
    solve()