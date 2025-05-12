import bisect

INF = int(10**9+1)

n, q = map(int, input().split())
tmp = [ (int(input()),i) for i in range(n) ]
tmp.sort()
s = [0]*n
f = [0]*n
i = 0
for key,val in tmp :
    s[i] = key
    f[val] = i
    i += 1

leader = []
while q > 0 :
    line = input().split()
    arg = int(line[1])
    #print(line)
    if line[0] == 'ADD':
        idx = bisect.bisect_left( leader, f[arg-1] )
        leader = leader[:idx] + [f[arg-1]] + leader[idx:]
    elif line[0] == 'REMOVE':
        leader.remove( f[arg-1] )
    else: #CHECK
        fail_r = -1
        succ_r = INF
        while succ_r - fail_r > 1 :
            mid = int((succ_r + fail_r)/2)
            count = 0
            prev = -1
            for idx in leader :
                l_idx = bisect.bisect_left( s, s[idx]-mid )
                r_idx = bisect.bisect_right( s, s[idx] ) - 1
                if l_idx <= prev : l_idx = prev + 1
                count += r_idx - l_idx + 1
                prev = r_idx

            if n - count <= arg : succ_r = mid
            else : fail_r = mid

        if succ_r == INF : print('NA')
        else : print(succ_r)

#    for idx in leader : print(idx)
    
    q -= 1