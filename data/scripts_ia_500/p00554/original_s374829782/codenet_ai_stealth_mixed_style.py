N,M=map(int,input().split())
A,B=[],[]
for _ in range(M):
    x,y=[int(i) for i in input().split()]
    A.append(x)
    B.append(y)
hit_card = sum(1 for a in A if a>=N)
need_money = 0
if hit_card < M-1:
    need_hit = (M-1)-hit_card
    sorted_A = sorted(A, reverse=True)
    i=0
    while i < need_hit:
        need_money += N - sorted_A[i + hit_card]
        i+=1
print(need_money)