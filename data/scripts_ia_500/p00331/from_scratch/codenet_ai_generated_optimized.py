H, R = map(int, input().split())
if H == -R:
    print(0)
elif H > -R:
    print(1)
else:
    print(-1)