n = int(input())
c = []#料理Nに対する高橋くんと青木さんの幸福度の和？
bs = 0#全ての料理を青木さんが食べたと仮定した時の青木さんの幸福度
for i in range(n):
    a,b = map(int,input().split())
    bs += b
    c.append(a+b)

c.sort()#Cを昇順ソート
c.reverse()#降順に直す

ans = -bs
for i in range(n):
    if i%2==0: ans += c[i]#高橋くんが食べる時、引いた青木さんの幸福度(食べてないのでいらない)と高橋くんの幸福度を足す
print(ans)