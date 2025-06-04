n=int(input())
heights=[float(input()) for _ in range(n)]
counts=[0]*6
for h in heights:
    if h<165: counts[0]+=1
    elif h<170: counts[1]+=1
    elif h<175: counts[2]+=1
    elif h<180: counts[3]+=1
    elif h<185: counts[4]+=1
    else: counts[5]+=1
for i,c in enumerate(counts,1):
    print(f"{i}:{'*'*c}")