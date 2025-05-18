def width(X,Y,x):
     n = len(X)
     lb,ub = float('inf'),-float('inf')
     for i in range(n):
          x1,y1,x2,y2 = X[i],Y[i],X[(i+1)%n],Y[(i+1)%n]
          if (x1-x)*(x2-x) <= 0 and x1 != x2:
               y = y1 + (y2-y1)*(x-x1)/(x2-x1)
               lb = min(lb,y)
               ub = max(ub,y)
     return max(0,ub-lb)

while 1:
     M,N = map(int,input().split())
     if not (M and N):
          break
     X1 = [0]*M
     Y1 = [0]*M
     X2 = [0]*N
     Z2 = [0]*N
     XS = [0]*N
     for i in range(M):
          X1[i],Y1[i] = map(int,input().split())
     for i in range(N):
          X2[i],Z2[i] = map(int,input().split())
     XS = X1+X2
     XS.sort()
     min1,max1 = min(X1),max(X1)
     min2,max2 = min(X2),max(X2)
     res = 0
     for i in range(len(XS)-1):
          a = XS[i]
          b = XS[i+1]
          c = (a+b)/2
          if min1 <= c <= max1 and min2 <= c <= max2:
               fa = width(X1,Y1,a)*width(X2,Z2,a)
               fb = width(X1,Y1,b)*width(X2,Z2,b)
               fc = width(X1,Y1,c)*width(X2,Z2,c)
               res += (b-a)/6 * (fa+4*fc+fb)
     print('%.10f'%res)