from collections import deque

base_char = ord('a')

while True:
    N = int(input())
    if N == 0:
        break

    graph = [[] for _ in range(26)]
    start_count = [0] * 26
    end_count = [0] * 26

    for _ in range(N):
        word = input().strip()
        start = ord(word[0]) - base_char
        end = ord(word[-1]) - base_char
        start_count[start] += 1
        end_count[end] += 1
        graph[start].append(end)

    # Check if in-degree == out-degree for all letters used
    possible = True
    for i in range(26):
        if start_count[i] != end_count[i]:
            possible = False
            break  # no need to check further if mismatch found

    if possible:
        visited = [False] * 26
        queue = deque()
        # find first node with some edges to start BFS
        for i in range(26):
            if start_count[i] > 0:
                queue.append(i)
                visited[i] = True
                break

        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if not visited[w]:
                    visited[w] = True
                    queue.append(w)

        # ensure all nodes with edges are connected
        for i in range(26):
            if start_count[i] > 0 and not visited[i]:
                possible = False
                break

    print("OK" if possible else "NG")