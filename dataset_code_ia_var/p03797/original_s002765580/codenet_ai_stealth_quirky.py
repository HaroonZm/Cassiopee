N,M=[int(_) for _ in input().split()]
get_x=lambda n,m:max(0,(m-n*2)//4)
weird_min=[N+get_x(N,M),M//2][0] if (N+get_x(N,M)) < (M//2) else [N+get_x(N,M),M//2][1]
print(weird_min)