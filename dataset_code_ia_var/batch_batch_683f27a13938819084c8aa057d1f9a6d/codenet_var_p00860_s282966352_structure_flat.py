from heapq import heappush, heappop
from itertools import product
from sys import stdin
file_input = stdin

while True:
    w, h, n = map(int, file_input.readline().split())
    if w == 0:
        break
    h -= 2
    w -= 2
    m = ""
    m_size = h * w
    file_input.readline()
    for i in range(h):
        m += file_input.readline()[1:w+1]
    file_input.readline()
    adj = [[i] for i in range(m_size)]
    start = []
    goal = []
    for i in range(m_size):
        c = m[i]
        a = adj[i]
        if c == '#':
            continue
        row = i // w
        col = i % w
        if row > 0 and m[i - w] != '#':
            a.append(i - w)
        if row < (h - 1) and m[i + w] != '#':
            a.append(i + w)
        if col > 0 and m[i - 1] != '#':
            a.append(i - 1)
        if col < (w - 1) and m[i + 1] != '#':
            a.append(i + 1)
        if c.islower():
            start.append(i)
            goal.append(m.index(c.upper()))
    start = tuple(start)
    goal = tuple(goal)

    if n == 1:
        s = start[0]
        g = goal[0]
        memo0 = set()
        memo1 = set()
        memo0.add(s)
        memo1.add(g)
        step = {s: 0, g: 0}
        current_s = 0
        state = [(s, 0), (g, 1)]
        found = False
        while state and not found:
            t_state = state[:]
            state.clear()
            current_s += 1
            for pos, d in t_state:
                for next_pos in adj[pos]:
                    if d == 0:
                        mem = memo0
                        opp_mem = memo1
                    else:
                        mem = memo1
                        opp_mem = memo0
                    if next_pos in mem:
                        continue
                    if next_pos in opp_mem:
                        print(current_s + step[next_pos])
                        found = True
                        break
                    state.append((next_pos, d))
                    mem.add(next_pos)
                    step[next_pos] = current_s
                if found:
                    break
        continue

    path_cost = [[0] * m_size for _ in range(n)]
    for idx in range(n):
        g = goal[idx]
        p_c = path_cost[idx]
        for i in range(m_size):
            if m[i] == '#' or i == g:
                continue
            memo0 = set()
            memo1 = set()
            memo0.add(i)
            memo1.add(g)
            step = {i: 0, g: 0}
            current_s = 0
            state = [(i, 0), (g, 1)]
            found = False
            while state and not found:
                t_state = state[:]
                state.clear()
                current_s += 1
                for pos, d in t_state:
                    for next_pos in adj[pos]:
                        if d == 0:
                            mem = memo0
                            opp_mem = memo1
                        else:
                            mem = memo1
                            opp_mem = memo0
                        if next_pos in mem:
                            continue
                        if next_pos in opp_mem:
                            p_c[i] = current_s + step[next_pos]
                            found = True
                            break
                        state.append((next_pos, d))
                        mem.add(next_pos)
                        step[next_pos] = current_s
                    if found:
                        break

    if n == 2:
        if start == goal:
            print(0)
            continue
        pc1 = path_cost[0]
        pc2 = path_cost[1]
        h_cost = max(pc1[start[0]], pc2[start[1]])
        state = (h_cost, start)
        q = [state]
        step = [[0 for _ in range(m_size)] for _ in range(m_size)]
        step[start[0]][start[1]] = 1
        found = False
        while q and not found:
            h_cost, pos = heappop(q)
            p1, p2 = pos
            if pos == goal:
                print(step[p1][p2] - 1)
                found = True
                break
            nps1 = adj[p1]
            nps2 = adj[p2]
            for np1, np2 in product(nps1, nps2):
                if step[np1][np2] or np1 == np2 or pos == (np2, np1):
                    continue
                s = step[p1][p2]
                new_h_cost = s + max(pc1[np1], pc2[np2])
                new_state = (new_h_cost, (np1, np2))
                heappush(q, new_state)
                step[np1][np2] = s + 1
        continue

    if n == 3:
        if start == goal:
            print(0)
            continue
        pc1 = path_cost[0]
        pc2 = path_cost[1]
        pc3 = path_cost[2]
        h_cost = max(pc1[start[0]], pc2[start[1]], pc3[start[2]])
        state = (h_cost, start)
        q = [state]
        step = [[[0 for _ in range(m_size)] for _ in range(m_size)] for _ in range(m_size)]
        step[start[0]][start[1]][start[2]] = 1
        found = False
        while q and not found:
            h_cost, pos = heappop(q)
            p1, p2, p3 = pos
            if pos == goal:
                print(step[p1][p2][p3] - 1)
                found = True
                break
            nps1 = adj[p1]
            nps2 = adj[p2]
            nps3 = adj[p3]
            for np1, np2, np3 in product(nps1, nps2, nps3):
                if step[np1][np2][np3]:
                    continue
                if np1 == np2 or np2 == np3 or np3 == np1:
                    continue
                if (p1, p2) == (np2, np1) or (p3, p1) == (np1, np3) or (p2, p3) == (np3, np2):
                    continue
                s = step[p1][p2][p3]
                new_h_cost = s + max(pc1[np1], pc2[np2], pc3[np3])
                new_state = (new_h_cost, (np1, np2, np3))
                heappush(q, new_state)
                step[np1][np2][np3] = s + 1
        continue