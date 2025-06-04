N = int(input())
print(min([sum(map(int, input().split())) for _ in range(N)]))