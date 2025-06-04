n,m=map(int,input().split())
if n==1:
    print(m//2)
    exit()
if n%2==1:
    # median at (n+1)//2-th element
    # to maximize |mean - median|, put 0s and m's to push median to 0 or m, and rest accordingly
    # Try median = 0:
    a=[0]*((n+1)//2)+[m]*((n-1)//2)
    sum_a=sum(a)
    # Adjust last element if needed
    a[(n+1)//2-1]=0
    # Now mean=sum_a/n; median=0; difference = mean - median = mean (positive or negative)
    # To maximize difference, we can also try median = m:
    b=[0]*((n-1)//2)+[m]*((n+1)//2)
    # difference = mean - median
    mean_a=sum(a)/n
    median_a=0
    diff_a=abs(mean_a-median_a)
    mean_b=sum(b)/n
    median_b=m
    diff_b=abs(mean_b-median_b)
    if diff_a>=diff_b:
        print(*a)
    else:
        print(*b)
else:
    # even n, median is average of two middle elements: n//2-th and n//2+1-th (1-based)
    # We can set these two middle elements to 0 and m to maximize difference
    # Construct a with median = 0
    a=[0]*(n//2)+[m]*(n//2)
    median_a= (a[(n//2)-1]+a[n//2])/2
    mean_a=sum(a)/n
    diff_a=abs(mean_a - median_a)
    # Construct b with median = m
    b=[0]*(n//2)+[m]*(n//2)
    # Swap middle elements for median m
    b[(n//2)-1]=m
    b[n//2]=m
    median_b=(b[(n//2)-1]+b[n//2])/2
    mean_b=sum(b)/n
    diff_b=abs(mean_b - median_b)
    if diff_a>=diff_b:
        print(*a)
    else:
        print(*b)