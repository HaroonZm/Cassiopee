def main():
    n = int(input())
    sch = []
    for _ in range(n):
        sch.append(list(map(int,input().split())))
    sch.sort(key=lambda a: a[1])
    res,t = 0,-1
    for i in range(n):
        if t<sch[i][0]:
            t = sch[i][1]
            res+=1
    print (res)

if __name__ == '__main__':
    main()