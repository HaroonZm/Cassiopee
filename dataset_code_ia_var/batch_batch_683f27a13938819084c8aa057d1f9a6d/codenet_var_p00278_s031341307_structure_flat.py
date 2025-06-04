import bisect
import sys

f = sys.stdin

n, q = (int(i) for i in f.readline().split())
s = [int(f.readline()) for _ in range(n)]
query = [line.split() for line in f]

sort_s = sorted(s)
leader = []

for idx in range(len(query)):
    op, a = query[idx]
    a = int(a)
    if op[0] == 'A':
        leader.append(s[a - 1])
        leader.sort()
    elif op[0] == 'R':
        leader.remove(s[a - 1])
    else:
        # check() inline
        if len(leader) == 0:
            if a < len(sort_s):
                print('NA')
            else:
                print(0)
            continue

        min_x = len(sort_s) - bisect.bisect_right(sort_s, leader[-1])
        if a < min_x:
            print('NA')
            continue

        l, r = 0, sort_s[-1]
        diff = r - 1
        while True:
            m = (l + r) // 2
            # get_count() inline
            count = 0
            pre_upper_pos = 0
            for li in leader:
                lower_pos = bisect.bisect_left(sort_s, li - m)
                upper_pos = bisect.bisect_right(sort_s, li)
                if pre_upper_pos < lower_pos:
                    count += lower_pos - pre_upper_pos
                pre_upper_pos = upper_pos
            count += len(sort_s) - pre_upper_pos
            x = count
            if a < x:
                l = m
            elif x <= a:
                r = m
            if diff == l - r:
                print(r)
                break
            diff = l - r