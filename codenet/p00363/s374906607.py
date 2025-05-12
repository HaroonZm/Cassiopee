W,H,c = input().split()
W = int(W)
H = int(H)

for i in range(H):
    for j in range(W):
        if (i == 0 or i == H-1) and (j == 0 or j == W-1):
            print("+", end="")
        elif i == 0 or i == H-1:
            print("-", end="")
        elif j == 0 or j == W-1:
            print("|", end="")
        elif 2*i == H-1 and 2*j == W-1:
            print(c, end="")
        else:
            print(".", end="")
    print("")