from bisect import bisect_left

def solve():
    n = int(input())
    # Generate triangular numbers up to just past 'n'
    tri_nums = [0]
    s = 0
    for i in range(1, int((2*n)**0.5)+3):
        s += i
        tri_nums.append(s)
        if s >= n:
            break

    idx = bisect_left(tri_nums, n)
    if idx >= len(tri_nums) or tri_nums[idx] != n:
        print('No')
        return

    k = idx
    from itertools import combinations

    ans = [[] for _ in range(k)]
    for cnt, (i, j) in enumerate(combinations(range(k), 2), 1):
        ans[i].append(cnt)
        ans[j].append(cnt)
    print('Yes')
    print(k)
    print('\n'.join(f"{k-1} {' '.join(map(str, row))}" for row in ans))

solve()