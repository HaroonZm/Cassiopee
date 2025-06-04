while True:
    R0, W0, C, R = map(int, input().split())
    if R0 == 0 and W0 == 0 and C == 0 and R == 0:
        break
    #濃度を今のままでOKならX=0
    if R0 * 1.0 / W0 == C:
        print(0)
        continue
    #X個のルウを足して濃度Cにするには
    # (R0 + X * R) / (W0 + Y) = C となるY>=0を探す
    #つまり Y = ((R0 + X*R)/C) - W0
    #Yが0以上ならXはOK
    #よってXを0から増やしながらY>=0になる最小のXを探す
    X = 0
    while True:
        Y = (R0 + X * R) / C - W0
        if Y >= 0:
            print(X)
            break
        X += 1