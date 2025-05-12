def get_count(s, leader, r):
    count = 0
    
    pre_upper_pos = 0
    
    for li in leader:
        lower_pos = bisect.bisect_left(s, li - r)
        upper_pos = bisect.bisect_right(s, li)
        if pre_upper_pos < lower_pos:
            count += lower_pos - pre_upper_pos
        pre_upper_pos = upper_pos
    count += len(s) - pre_upper_pos
    
    return count

import bisect

def check(s,leader,target_x):
    if 0 == len(leader):
        if target_x < len(s):
            return 'NA'
        else:
            return 0
    min_x = len(s) - bisect.bisect_right(s, leader[-1])
    if target_x < min_x:
        return 'NA'

    l, r = 0, s[-1]
    diff = r - 1
    while True:
        m = (l + r) // 2
        x = get_count(s, leader, m)
        if target_x < x:
            l = m
        elif x <= target_x:
            r = m
        
        if diff == l - r:
            return r
        diff = l - r

import sys
f = sys.stdin

n, q = (int(i) for i in  f.readline().split())
s = [int(f.readline()) for i in range(n)]
query = [line.split() for line in f]

sort_s = sorted(s)
leader = []

for op, a in query:
    a = int(a)
    if op[0] == 'A':
        leader.append(s[a - 1]) #bisect??§??????????¶?????????????????????\?????????
        leader.sort()
    elif op[0] == 'R':
        leader.remove(s[a - 1])
    else:
        r = check(sort_s,leader,a)
        print(r)