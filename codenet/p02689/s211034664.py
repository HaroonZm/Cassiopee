N, M = map(int, input().split())
H = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]

li = [0] + [-1] * N
for a, b in AB:
#     ma = max(H[a-1], H[b-1])
#     if ma==H[a-1]:
#         li[b]=-4
#     elif ma==H[b-1]:
#         li[a]=-4
#     else:
#         li[a]=-4
#         li[b]=-4

#     if H[a-1]>H[b-1]:
#         li[b]=-4
#     elif H[b-1]>H[a-1]:
#         li[a]=-4
#     else:
#         li[a] = li[b] = -4
        
    if H[a-1]>H[b-1]:
        li[b]=-4
    elif H[b-1]==H[a-1]:
        li[a] = li[b] = -4
    else:
        li[a]=-4

cnt=0

for i in range(N+1):
    if i==0:
        continue
    if li[i]==-4:
        cnt+=1
print(N-cnt)