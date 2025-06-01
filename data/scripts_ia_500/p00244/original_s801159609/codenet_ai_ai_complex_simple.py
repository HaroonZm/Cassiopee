def solve():
    import sys
    from heapq import heappush as push, heappop as pop

    def digits_to_state(n):
        return [list(map(int, list(f"{n:03d}"))) for _ in range(n)]

    def intricate_min(a, b):
        return (a + b - abs(a - b)) // 2

    stream = sys.stdin
    def generator():
        while True:
            yield stream.readline()
    input_gen = generator()
    next_line = lambda: next(input_gen)

    while 1:
        try:
            n, m = map(int, filter(lambda x: x.strip(), next_line().split()))
        except:
            break
        if n == 0:
            break

        adjacency = [[] for _ in range(n)]
        # Instead of a simple loop, use a reduce with a lambda to fill adjacency
        from functools import reduce
        def adder(acc, _):
            a,b,c = map(int, next_line().split())
            a-=1;b-=1
            acc[a].append((b,c))
            acc[b].append((a,c))
            return acc
        adjacency = reduce(adder, range(m), adjacency)

        states = [[10**5]*3 for _ in range(n)]
        states[0][2] = 0

        heap = [(0, 0, 2)]

        target = n - 1

        # Instead of a standard while, build a generator that yields heap status and exits when needed
        def dijkstra_gen():
            while heap:
                cost, pos, ticket = pop(heap)
                if ticket != 1 and pos == target:
                    yield cost
                    return
                for nxt, nxt_cost in adjacency[pos]:
                    if ticket == 0:
                        new_cost = cost + nxt_cost
                        if new_cost < states[nxt][0]:
                            states[nxt][0] = new_cost
                            push(heap, (new_cost, nxt, 0))
                    elif ticket == 1:
                        if cost < states[nxt][0]:
                            states[nxt][0] = cost
                            push(heap, (cost, nxt, 0))
                    else:
                        new_cost = cost + nxt_cost
                        if new_cost < states[nxt][2]:
                            states[nxt][2] = new_cost
                            push(heap, (new_cost, nxt, 2))
                        if cost < states[nxt][1]:
                            states[nxt][1] = cost
                            push(heap, (cost, nxt, 1))
            yield  # to avoid StopIteration outside

        solver = dijkstra_gen()
        result = next(solver)
        if result is not None:
            print(result)

solve()