from sys import stdin
N = stdin.readline().rstrip()

N=str(N)
o=0
if len(N)==4:
    if N[0]=="2": o+=1
    if N[1]=="2": o+=1  
    if N[2]=="2": o+=1  
    if N[3]=="2": o+=1  

print(o)