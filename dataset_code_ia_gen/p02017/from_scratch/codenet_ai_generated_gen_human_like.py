H, W, X, Y = map(int, input().split())
if (H * W) % 2 == 1 and (X + Y) % 2 == 1:
    print("No")
else:
    print("Yes")