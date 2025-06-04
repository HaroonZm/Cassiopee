import sys
from operator import itemgetter

def read_ints():
    return map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline())
sec = [tuple(read_ints()) for _ in range(N)]
left = sorted(((l, i) for i, (l, _) in enumerate(sec)), key=itemgetter(0))
right = sorted(((r, i) for i, (_, r) in enumerate(sec)), key=itemgetter(0), reverse=True)

def process_paths(left_input, right_input, odd_first=True):
    used = [False] * N
    ls, rs = left_input.copy(), right_input.copy()
    pos, ans, n = 0, 0, 0
    flag_l, flag_r = 0, 0
    parity = 1 if odd_first else 0
    while ls or rs:
        if n % 2 == parity:
            curr = ls
            cmp_idx = 0  # left value
            flag, flag_assign = flag_l, 'flag_l'
        else:
            curr = rs
            cmp_idx = 0  # right value
            flag, flag_assign = flag_r, 'flag_r'
        if not curr:
            n += 1
            continue
        val, idx = curr[-1]
        if used[idx]:
            curr.pop()
            continue
        if (n % 2 == parity and pos < val) or (n % 2 != parity and pos > val):
            ans += abs(val - pos)
            pos = val
            used[idx] = True
            curr.pop()
            if n % 2 == parity:
                flag_l = 0
            else:
                flag_r = 0
        else:
            if flag == 1:
                curr.pop()
                if n % 2 == parity:
                    flag_l = 0
                else:
                    flag_r = 0
            else:
                if n % 2 == parity:
                    flag_l = 1
                else:
                    flag_r = 1
        n += 1
    return ans + abs(pos)

ans1 = process_paths(left, right, odd_first=False)
ans2 = process_paths(left, right, odd_first=True)
print(max(ans1, ans2))