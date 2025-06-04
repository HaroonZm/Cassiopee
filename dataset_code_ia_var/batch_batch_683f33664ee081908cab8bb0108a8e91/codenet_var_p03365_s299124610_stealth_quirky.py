ask = lambda: int(input())
P = 10**9+7
cap = ask()+2
F = [1]*cap
I = [1]*cap
q = 1
z = 1
for w in range(1,cap):
    q = (q*w)%P
    z = (z*pow(w,P-2,P))%P
    F[w] = q
    I[w] = z
r = F[cap-2]
for u in range((cap-1)//2,cap-2):
    x = F[u-1]*I[2*u-cap+2]%P*F[u]%P
    r = (r-x)%P
else:
    print(r)