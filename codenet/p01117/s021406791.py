for i in range(110):
    x,y = map(int,input().split()) #xは生徒,yは科目
    if x == y == 0:
        break
    else:
        a = [0]*x
        for j in range(y):
            ls = list(map(int,input().split()))
            for _ in range(x):
                a[_] += ls[_]
        print(max(a))