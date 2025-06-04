while True:
    data = input().split()
    if len(data) == 1 and data[0] == '0':
        break
    q1, b, c1, c2, q2 = map(int, data)
    found = False
    # 会津地鶏の購入量xをq1以上q2以下で探す
    # 会津地鶏は必ず買うのでx >= q1かつx <= q2
    for x in range(q1, q2+1):
        costA = x * c1
        if costA > b:
            continue
        remain = b - costA
        # ふつうの鶏肉の最大購入量y
        y = remain // c2
        # yは100g単位であり、量は整数
        # 合計量x + y >= q1の条件はx>=q1で満たされているので無視して良い
        # 必要量を満たしつつ、なるべく会津地鶏を多く買うためxを増やして最初に見つけた解で良い
        # ふつうの鶏肉はできるだけ多く買うのでこのyで良い
        found = True
        print(x, y)
        break
    if not found:
        print("NA")