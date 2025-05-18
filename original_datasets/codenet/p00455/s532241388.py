for i in range(3):
        h,m,s,nh,nm,ns = map(int,input().split())
        t = nh * 3600 + nm * 60 + ns - (h * 3600 + m * 60 + s)
        h = t // 3600
        m = t % 3600 // 60
        s = t % 60
        print(h,m,s)