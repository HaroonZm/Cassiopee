for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    t = h2*3600+m2*60+s2-h1*3600-m1*60-s1
    print(t//3600, (t%3600)//60, t%60)