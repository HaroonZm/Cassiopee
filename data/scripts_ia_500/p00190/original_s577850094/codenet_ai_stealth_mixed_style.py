from heapq import heappush, heappop

comp = [(1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (1, 3), (2, 3), (3, 3)]
numbers = range(11)
zeros = (11, 12)

def manhattan(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return abs(x1 - x2) + abs(y1 - y2)

def heuristic(state):
    total = 0
    for i in numbers:
        total += manhattan(state[i], comp[i])
    return total

def swaped(state, n1, n2):
    from copy import deepcopy
    ns = list(state)
    ns[n1], ns[n2] = ns[n2], ns[n1]
    return tuple(ns)

def main():
    while True:
        p1 = input()
        if p1.strip() == '-1':
            break
        p1 = int(p1)
        l1 = [-1, -1, p1, -1, -1]
        l2 = [-1]
        for x in input().split():
            l2.append(int(x))
        l2.append(-1)
        l3 = list(map(int, input().split()))
        l4 = [-1] + list(map(int, input().split())) + [-1]
        l5 = [-1, -1, int(input()), -1, -1]
        mp = [l1, l2, l3, l4, l5]
        init_state = [None]*13

        for y in range(5):
            for x in range(5):
                if mp[y][x] != -1:
                    val = mp[y][x]
                    if val == 0:
                        if init_state[11] is None:
                            init_state[11] = (x, y)
                        else:
                            init_state[12] = (x, y)
                    else:
                        init_state[val - 1] = (x, y)

        init_state = tuple(init_state)
        visited = {init_state}
        pq = []
        heappush(pq, (heuristic(init_state), 0, init_state))

        solved = False
        while pq:
            est, steps, state = heappop(pq)
            if est - steps == 0:
                print(steps)
                solved = True
                break
            for z in zeros:
                for i in numbers:
                    if manhattan(state[z], state[i]) == 1:
                        new_state = swaped(state, i, z)
                        if new_state not in visited:
                            visited.add(new_state)
                            cost = heuristic(new_state) + steps + 1
                            if cost <= 20:
                                heappush(pq, (cost, steps + 1, new_state))
        if not solved:
            print("NA")

if __name__ == "__main__":
    main()