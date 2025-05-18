def solve():
    from sys import stdin
    f_i = stdin
    
    ans = ''
    
    while True:
        n, m = map(int, f_i.readline().split())
        if n == 0:
            break
        
        # prep for warshall-floyd algorithm
        inf = 10000 * 31 + 1
        dist = [[inf] * n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        for i in range(m):
            s, t, d = map(int, f_i.readline().split())
            s -= 1
            t -= 1
            dist[s][t] = d
            dist[t][s] = d
        
        # table for path reconstruction
        next_p = [list(range(n)) for i in range(n)]
        
        # Warshall-Floyd algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d_ikj = dist[i][k] + dist[k][j]
                    d_ij = dist[i][j]
                    if d_ikj < d_ij:
                        dist[i][j] = d_ikj
                        next_p[i][j] = next_p[i][k]
                    # for restore the smallest path in lexicographic order
                    elif k != i and d_ikj == d_ij:
                        if next_p[i][k] < next_p[i][j]:
                            next_p[i][j] = next_p[i][k]
        
        l = int(f_i.readline())
        paths = []
        mails = set()
        messages = []
        goals = []
        for i in range(l):
            start, goal, at, msg = f_i.readline().split()
            start = int(start) - 1
            goal = int(goal) - 1
            at = int(at)
            messages.append(msg)
            goals.append(goal)
            
            # path reconstruction
            path = []
            cur = start
            while cur != goal:
                path.append(cur)
                cur = next_p[cur][goal]
            path.append(goal)
            
            paths.append(path)
            # mail: (time, arrivalTime, next, cur, number)
            mails.add((at, at, path[1], start, i))
        
        step = [1] * l
        deliv_time = [0] * n
        
        # mail forwarding
        tmp_ans = []
        while mails:
            t, at, nxt, cur, num = min(mails)
            
            to_forward = set(filter(lambda x: x[0] == t and x[2] == nxt and x[3] == cur, mails))
            mails = mails.difference(to_forward)
            
            dt = deliv_time[cur]
            # transferable
            if t >= dt:
                cost = dist[cur][nxt]
                new_t = t + cost
                for t, at, nxt, cur, num in to_forward:
                    if nxt == goals[num]:
                        tmp_ans.append((new_t, messages[num]))
                    else:
                        step[num] += 1
                        new_nxt = paths[num][step[num]]
                        mails.add((new_t, new_t, new_nxt, nxt, num))
                deliv_time[cur] = t + cost * 2
            # non-transferable
            else:
                for t, at, nxt, cur, num in to_forward:
                    mails.add((dt, at, nxt, cur, num))
        
        tmp_ans.sort()
        tmp_ans = (f"{label} {time}" for time, label in tmp_ans)
        ans += '\n'.join(tmp_ans) + '\n\n'
    
    print(ans.rstrip())

solve()