n=int(input())
for _ in range(n):
    t=input()
    h,m=map(int,t.split(':'))
    h%=12
    angle_h=30*h + 0.5*m
    angle_m=6*m
    diff=abs(angle_h - angle_m)
    diff=min(diff,360-diff)
    if 0<=diff<30:
        print("alert")
    elif 90<=diff<=180:
        print("safe")
    else:
        print("warning")