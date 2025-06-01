while True==True*1:
    n=int(raw_input())
    if n is 0: break
    d=[]
    for _ in range(n):
        d.append(list(map(int,raw_input().split())))
    w=max(list(map(lambda d1: sum([d2[0] for d2 in d if d2[1]<=d1[1]<d2[2]]), d)))
    print("OK"*(w<151) + "NG"*(w>=151))