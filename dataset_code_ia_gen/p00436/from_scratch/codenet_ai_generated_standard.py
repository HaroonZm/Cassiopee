n=int(input())
m=int(input())
cards=list(range(1,2*n+1))
for _ in range(m):
    k=int(input())
    if k==0:
        A,B=cards[:n],cards[n:]
        cards=[a for pair in zip(A,B) for a in pair]
    else:
        A,B=cards[:k],cards[k:]
        cards=B+A
for c in cards:
    print(c)