n=int(input())
for _ in range(n):
    hh,mm=map(int,input().split(':'))
    h_angle=(hh%12)*30+mm*0.5
    m_angle=mm*6
    diff=abs(h_angle-m_angle)
    diff=min(diff,360-diff)
    if 0<=diff<30:
        print("alert")
    elif 90<=diff<=180:
        print("safe")
    else:
        print("warning")