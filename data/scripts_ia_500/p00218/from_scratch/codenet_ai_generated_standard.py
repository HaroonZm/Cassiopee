while True:
    n=int(input())
    if n==0:
        break
    for _ in range(n):
        pm,pe,pj=map(int,input().split())
        avg=(pm+pe+pj)/3
        if pm==100 or pe==100 or pj==100:
            print('A')
        elif (pm+pe)/2>=90:
            print('A')
        elif avg>=80:
            print('A')
        elif avg>=70:
            print('B')
        elif avg>=50 and (pm>=80 or pe>=80):
            print('B')
        else:
            print('C')