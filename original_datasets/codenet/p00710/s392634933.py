while 1:
    count, times = [int(a) for a in input().split()]
    hanahuda = [i+1 for i in range(count)]
    if count == times == 0:break
    for i in [0]*times:
        p,c = [int(i) for i in input().split()]
        for i in [0]*c:hanahuda.append(hanahuda.pop(count-(p+c)+1))
    print(hanahuda.pop())