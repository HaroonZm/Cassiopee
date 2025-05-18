while True:
    H,W=map(int,input().split())
    if H==0 & W==0:
        break
    shape_dot='#.'*W
    dot_shape='.#'*W
    for i in range(H):
        if i %2 ==0:
            print(shape_dot[:W])

        else:
            print(dot_shape[:W])

    print('')