H=int(input())
A=[0]+list(map(int,input().split()))
for i in range(1,H+1):
    out = f"node {i}: key = {A[i]}, "
    if i//2>0:
        out += f"parent key = {A[i//2]}, "
    if 2*i <= H:
        out += f"left key = {A[2*i]}, "
    if 2*i+1 <= H:
        out += f"right key = {A[2*i+1]}, "
    print(out)