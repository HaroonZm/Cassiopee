import sys
input=sys.stdin.readline
while True:
    n=int(input())
    if n==0:
        break
    counts=[0]*7
    for _ in range(n):
        a=int(input())
        if a<10:
            counts[0]+=1
        elif a<20:
            counts[1]+=1
        elif a<30:
            counts[2]+=1
        elif a<40:
            counts[3]+=1
        elif a<50:
            counts[4]+=1
        elif a<60:
            counts[5]+=1
        else:
            counts[6]+=1
    print('\n'.join(map(str,counts)))