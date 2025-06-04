import sys
for line in sys.stdin:
    n,k,m = map(int,line.split())
    if n==0 and k==0 and m==0:
        break
    # Adjust m to zero-based index
    pos = m - 1
    for i in range(n,1,-1):
        pos = (pos + k - 1) % i
    print(pos+1)