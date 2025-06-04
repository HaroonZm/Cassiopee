M, N = map(int, input().split())
max_solved = 0
for _ in range(M):
    solved = sum(map(int, input().split()))
    if solved > max_solved:
        max_solved = solved
print(max_solved)