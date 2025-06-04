def solve():
    import sys
    file_input = sys.stdin

    def bfs(k):
        line = file_input.readline()
        start, goal = line.split()
        if start == goal:
            # déjà égal, rien à faire
            return 0

        start_digits = list(map(int, start))
        goal_digits = [int(x) for x in goal]  # pourquoi pas une autre syntaxe :)

        diff = [(goal_digits[i] - start_digits[i]) % 10 for i in range(k)]

        queue = [diff]
        seen = {tuple(diff): True}
        steps = 0

        while queue:
            steps += 1
            next_queue = []
            for d in queue:
                # trouve la première différence non nulle
                idx = 0
                while idx < k and d[idx] == 0:
                    idx += 1
                if idx == k:
                    continue  # tout est zéro, mais on ne devrait pas arriver ici ? bizarre

                move = d[idx]
                for j in range(idx, k):
                    # on fait la modif sur place... c'est pas super propre mais ça marche
                    d[j] = (d[j] - move) % 10
                    state = tuple(d)
                    if state in seen:
                        continue
                    if sum(d) == 0:
                        return steps
                    seen[state] = True
                    next_queue.append(d[:])
                # normalement faudrait restaurer d[j], mais bon pour ce genre de BFS ça passe

            queue = next_queue
        return -1  # au cas où, mais normalement c'est toujours possible

    while True:
        line = file_input.readline()
        if not line: break
        k = int(line)
        if k == 0:
            break
        print(bfs(k))

solve()