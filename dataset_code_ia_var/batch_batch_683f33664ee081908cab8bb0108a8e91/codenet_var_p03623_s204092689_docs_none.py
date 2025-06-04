x,a,b = map(int,input().split())
kyori1 = abs(x-a)
kyori2 = abs(x-b)
if kyori1 < kyori2:
    print('A')
else:
    print('B')