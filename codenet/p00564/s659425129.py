from math import ceil
N,A,B,C,D = map(int,input().split())   #N A B C D
if ceil(N/A)*B > ceil(N/C)*D:
    print(ceil(N/C)*D)
elif ceil(N/C)*D > ceil(N/A)*B :
    print(ceil(N/A)*B)
else:
    print(ceil(N/A)*B)