n=int(input())
for i in range(n):
    hh,mm=map(int,input().split(":"))
    angleh=(60*hh+mm)*0.5
    anglem=6*mm
    diff=abs(angleh-anglem)
    if diff>180:diff=360-diff
    if 0<=diff<30:
        print("alert")
    elif 90<=diff<=180:
        print("safe")
    else:
        print("warning")