def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A = [0] + A + [0]

    edges = []
    going_up = True

    for i in range(1, len(A) -1):
        if going_up:
            if A[i] > A[i+1]:
                edges.append([A[i], going_up])
                going_up = False
        else:
            if A[i] < A[i+1]:
                edges.append([A[i], going_up])
                going_up = True

    edges.sort()

    island_count = 1
    max_islands = 1

    for i in range(len(edges) -1):
        if edges[i][1]:
            island_count -= 1
        else:
            island_count += 1

        if edges[i][0] < edges[i+1][0]:
            if island_count > max_islands:
                max_islands = island_count

    if max(A) <= 0:
        max_islands = 0

    print(max_islands)

if __name__ == "__main__":
    solve()