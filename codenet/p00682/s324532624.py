cnt=1
while True:
    n=input()
    if n==0:break
    data=[map(int,raw_input().split()) for i in range(n)]
    data.append(data[0])
    print cnt,sum((data[i][0]-data[i+1][0])*(data[i][1]+data[i+1][1]) for i in \
range(n))/(-2.0)
    cnt+=1
    skip=raw_input()