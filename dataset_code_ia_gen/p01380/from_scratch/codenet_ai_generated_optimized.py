import sys
input = sys.stdin.readline

N = int(input())
problems = [tuple(map(int, input().split())) for _ in range(N)]
problems.sort(key=lambda x: x[1])

time = 0
count = 0
for A, B in problems:
    time += A
    if time <= B:
        count += 1

print(count)