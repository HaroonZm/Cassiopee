N=int(input())
w=0
for h in range(1,3501):
    for n in range(h,3501):
        if 4*h*n>N*(h+n) and N*h*n%(4*h*n-N*(h+n))==0:
            w=N*h*n//(4*h*n-N*(h+n))
            break
    if w>0:
        break

print(h,n,w)