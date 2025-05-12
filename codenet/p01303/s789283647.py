for i in range(input()):
    X,Y,W,H=map(int,raw_input().split())
    cnt=0
    N=input()
    for	i in range(N):
	x,y=map(int,raw_input().split())
	if (X<=x<=X+W) and (Y<=y<=Y+H):
            cnt+=1
    print cnt