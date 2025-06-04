from sys import exit

N, K = map(int, input().split())
D = set(input().split())

for candidate in range(N, 10**6):
    if not set(str(candidate)) & D:
        print(candidate)
        exit()