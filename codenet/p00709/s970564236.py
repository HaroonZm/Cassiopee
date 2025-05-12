def solve():
    from itertools import combinations
    from sys import stdin
    file_input = stdin
    
    while True:
        W, H = map(int, file_input.readline().split())
        if W == 0:
            break
        
        carpets = []
        state = 0
        
        # Largest Square algorithm
        prev = [0] * (W + 1)
        for i in range(1, H + 1):
            f_line = file_input.readline().split()
            cur = [0] * (W + 1)
            for j, tpl in enumerate(zip(f_line, prev, prev[1:]), start=1):
                p, p1, p2 = tpl
                if p == '1':
                    side = min(p1, p2, cur[j - 1]) + 1
                    cur[j] = side
                    
                    # making carpet bit sequence
                    line_bit = (1 << side) - 1
                    line_bit <<= (j - side)
                    c_b = line_bit
                    for k in range(side - 1):
                        c_b <<= W
                        c_b += line_bit
                    c_b <<= (W * (i - side))
                    carpets.append(c_b)
                else:
                    b = 1 << (j - 1)
                    b <<= (W * (i - 1))
                    state += b
            prev = cur
        
        flag = -1
        ans = 0
        while flag != state:
            flag = state
            
            c_check = dict(zip(carpets, [False] * len(carpets)))
            for c1, c2 in combinations(carpets, 2):
                if c_check[c1] or c_check[c2]:
                    continue
                overlap = c1 & c2
                if overlap == c2:
                    c_check[c2] = True
                elif overlap == c1:
                    c_check[c1] = True
            carpets = []
            for k, v in c_check.items():
                if not v:
                    carpets.append(k)
            
            for i in range(W * H):
                b = 1 << i
                if b & state:
                    continue
                t_carpets = []
                for c in carpets:
                    if b & c:
                        t_carpets.append(c)
                if len(t_carpets) == 1:
                    c = t_carpets[0]
                    state |= c
                    ans += 1
                    carpets.remove(c)
            
            carpets = list(set(c^(c & state) for c in carpets))
            
        goal = (1 << (W*H)) - 1
        if state == goal:
            print(ans)
            continue
        
        for i in range(1, len(carpets) + 1):
            for t_carpets in combinations(carpets, i):
                t_state = state
                for c in t_carpets:
                    t_state |= c
                if t_state == goal:
                    print(ans + i)
                    break
                else:
                    continue
                break
            else:
                continue
            break

solve()