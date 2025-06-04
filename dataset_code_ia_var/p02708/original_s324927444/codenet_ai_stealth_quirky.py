M=10**9+7
exec("x,y=map(int,input().split())\nz=0\nfor Q in range(y,x+2):\n P=Q*(Q-1)//2\n S=x*(x+1)//2-(x-Q)*(x-Q+1)//2\n z=(z+S+1-P)%M\nprint(z)")