H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

for i in range(-1, H+1):
    if i == -1 or i == H:
        print("#" * (W+2))
    else:
        tmp = ["#"] + a[i] + ["#"]
        print("".join(tmp))