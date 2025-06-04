def solve():
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
        for i, t in enumerate(zip(m, adj)):
            c, a = t
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
            start = start[0]
            goal = goal[0]
            memo = [set(), set()]
            memo[0].add(start)
            memo[1].add(goal)
            step = {start: 0, goal: 0}
            s = 0
            state = [(start, 0), (goal, 1)]

            while state:
                t_state = state[:]
                state.clear()
                s += 1
                for pos, d in t_state:
                    for next_pos in adj[pos]:
                        if next_pos in memo[d]:
                            continue
                        if next_pos in memo[not d]:
                            print(s + step[next_pos])
                            t_state.clear()
                            state.clear()
                            break
                        state.append((next_pos, d))
                        memo[d].add(next_pos)
                        step[next_pos] = s
            continue

        path_cost = [[0] * m_size for i in range(n)]
        for g, p_c in zip(goal, path_cost):
            for i, p in enumerate(m):
                if p == '#' or i == g:
                    continue
                memo = [set(), set()]
                memo[0].add(i)
                memo[1].add(g)
                step = {i: 0, g: 0}
                s = 0
                state = [(i, 0), (g, 1)]

                while state:
                    t_state = state[:]
                    state.clear()
                    s += 1
                    for pos, d in t_state:
                        for next_pos in adj[pos]:
                            if next_pos in memo[d]:
                                continue
                            if next_pos in memo[not d]:
                                p_c[i] = s + step[next_pos]
                                t_state.clear()
                                state.clear()
                                break
                            state.append((next_pos, d))
                            memo[d].add(next_pos)
                            step[next_pos] = s

        h_cost = max(p_c[s] for s, p_c in zip(start, path_cost))

        if n == 2:
            if start == goal:
                print(0)
                continue
            state = (h_cost, start)
            q = [state]
            step = [[0 for j in range(m_size)] for i in range(m_size)]
            step[start[0]][start[1]] = 1
            pc1, pc2 = path_cost

            while q:
                h_cost, pos = heappop(q)
                p1, p2 = pos
                if pos == goal:
                    print(step[p1][p2] - 1)
                    break

                nps1, nps2 = adj[pos[0]], adj[pos[1]]
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
            state = (h_cost, start)
            q = [state]
            step = [[[0 for k in range(m_size)] for j in range(m_size)] for i in range(m_size)]
            step[start[0]][start[1]][start[2]] = 1
            pc1, pc2, pc3 = path_cost

            while q:
                h_cost, pos = heappop(q)
                p1, p2, p3 = pos
                if pos == goal:
                    print(step[p1][p2][p3] - 1)
                    break

                nps1, nps2, nps3 = adj[p1], adj[p2], adj[p3]
                for np1, np2, np3 in product(nps1, nps2, nps3):
                    if step[np1][np2][np3] or \
                    np1 == np2 or np2 == np3 or np3 == np1 or \
                    (p1, p2) == (np2, np1) or (p3, p1) == (np1, np3) or \
                    (p2, p3) == (np3, np2):
                        continue
                    s = step[p1][p2][p3]
                    new_h_cost = s + max(pc1[np1], pc2[np2], pc3[np3])
                    new_state = (new_h_cost, (np1, np2, np3))
                    heappush(q, new_state)
                    step[np1][np2][np3] = s + 1
            continue

solve()