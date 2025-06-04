n = int(input())
for _ in range(n):
    s = input()
    parts = []
    i = 0
    while i < len(s):
        if s[i].islower():
            parts.append(s[i])
            i += 1
        else:
            if s[i] == '-' and i+1 < len(s) and (s[i+1] == '<' or s[i+1] == '>'):
                parts.append(s[i:i+2])
                i += 2
            else:
                i += 1

    # Reconstruct edges according to moves
    edges = {}
    # edges will store adjacency: car -> (front_car, back_car)
    # but here we store neighbors: for each car, set of neighbors based on moves
    
    # From the moves, build adjacency list undirected graph
    for i in range(0, len(parts)-2, 2):
        car1 = parts[i]
        move = parts[i+1]
        car2 = parts[i+2]

        # If car1 not in edges, add empty set
        if car1 not in edges:
            edges[car1] = set()
        if car2 not in edges:
            edges[car2] = set()

        # According to direction, link car1 and car2
        # move '->' means car2 is after car1, link both ways for undirected graph
        # move '<-' means car2 is before car1, same as above, undirected

        edges[car1].add(car2)
        edges[car2].add(car1)

    # Find the ends of the train - cars that have only one neighbor
    ends = [car for car, neigh in edges.items() if len(neigh) == 1]

    # The train is a chain, so exactly two ends
    # We choose one end to start output

    start = ends[0]

    # Reconstruct the order by walking along edges
    order = [start]
    prev = None
    current = start

    while True:
        neighbors = edges[current]
        next_car = None
        for neigh in neighbors:
            if neigh != prev:
                next_car = neigh
                break
        if next_car is None:
            break
        order.append(next_car)
        prev = current
        current = next_car

    print("".join(order))