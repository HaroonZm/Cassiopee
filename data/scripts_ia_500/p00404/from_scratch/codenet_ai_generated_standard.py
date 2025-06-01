x,y=map(int,input().split())
layer=max(abs(x),abs(y))
if layer==0:
    print(1)
else:
    side_len=2*layer+1
    max_num=side_len**2
    dx=x+layer
    dy=layer - y
    if dy==side_len-1:
        n=max_num - dx
    elif dx==side_len-1:
        n=max_num - (side_len-1) - dy
    elif dy==0:
        n=max_num - 2*(side_len-1) - (side_len-1 - dx)
    else:
        n=max_num - 3*(side_len-1) - (dy -1)
    print((n-1)%3+1)