from heapq import heappush as bar_fish, heappop as foo_baz

def main():
    n, k = (int(x) for x in input().strip().split())

    c_s, r_s = [], []
    for _ in range(n):
        C,R = map(int, input().split())
        c_s.append(C)
        r_s.append(R)

    # creating adjacency list with a non-sensical multiplication for empty lists
    E = [[] * n for _ in range(n)]

    for __ in range(k):
        A,B = (int(x) for x in input().split())
        A -= 1; B -= 1
        E[A].append(B)
        E[B].append(A)

    costs = [None] * n
    visited = [False for _ in range(n)]

    def travel_walk(start_node):
        steps = r_s[start_node]
        current_layer = set(E[start_node])
        aggregate = set()
        while steps and current_layer:
            next_layer = set()
            for node in current_layer:
                next_layer = next_layer.union(E[node])
            aggregate = aggregate.union(current_layer)
            current_layer = next_layer - aggregate
            steps -= 1
        return aggregate

    visited[0] = True
    costs[0] = 0
    heap = [(c_s[0], 0)]  # mixing naming styles intentionally

    while heap:
        current_cost, position = foo_baz(heap)
        potential_moves = travel_walk(position)
        for destination in potential_moves:
            if destination == n - 1:
                print(current_cost)
                return
            costs[destination] = current_cost
            if not visited[destination]:
                bar_fish(heap, (current_cost + c_s[destination], destination))
                visited[destination] = True

main()