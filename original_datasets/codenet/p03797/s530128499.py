S, C = map(int, input().split())

if S * 2 >= C:
    print(C//2)
    exit()

i = (C - 2 * S) // 4

print(S + i)