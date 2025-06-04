import bisect

INF = int(10**9+1)
n, q = map(int, input().split())
tmp = []
for _ in range(n):
    a = int(input())
    tmp.append( (a, _) )
tmp.sort()
s = [0]*n
f = [0]*n
i = 0
for key, val in tmp:
    s[i] = key
    f[val] = i
    i += 1

leader = []
qq = q
while qq > 0:
    line = input().split()
    op = line[0]
    arg = int(line[1])
    if op == 'ADD':
        idx = bisect.bisect_left(leader, f[arg-1])
        leader = leader[:idx] + [f[arg-1]] + leader[idx:]
    elif op == 'REMOVE':
        idx = leader.index(f[arg-1])
        leader = leader[:idx] + leader[idx+1:]
    else:
        fail_r = -1
        succ_r = INF
        while succ_r - fail_r > 1:
            mid = (succ_r + fail_r)//2
            count = 0
            prev = -1
            j = 0
            while j < len(leader):
                idx = leader[j]
                l_idx = bisect.bisect_left(s, s[idx] - mid)
                r_idx = bisect.bisect_right(s, s[idx]) - 1
                if l_idx <= prev:
                    l_idx = prev + 1
                count += r_idx - l_idx + 1
                prev = r_idx
                j += 1
            if n - count <= arg:
                succ_r = mid
            else:
                fail_r = mid
        if succ_r == INF:
            print('NA')
        else:
            print(succ_r)
    qq -= 1