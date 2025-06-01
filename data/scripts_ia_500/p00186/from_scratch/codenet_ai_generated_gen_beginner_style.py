while True:
    data = input().split()
    if len(data) == 1 and data[0] == '0':
        break
    q1 = int(data[0])
    b = int(data[1])
    c1 = int(data[2])
    c2 = int(data[3])
    q2 = int(data[4])

    # q1: minimum total amount (100g units)
    # b: budget
    # c1: price of 会津地鶏 per 100g
    # c2: price of normal chicken per 100g
    # q2: max 会津地鶏 buyer can buy (100g units)

    ans_aizudori = -1
    ans_normal = -1

    # 会津地鶏は必ず買う。0はダメ。
    # 会津地鶏は最大q2まで
    # 合計量がq1以上
    # 予算内
    # 会津地鶏をできるだけ多く、それからふつうの鶏肉。

    # 会津地鶏を多く買うのでq2から1まで減らして探す
    for aizudori in range(min(q2, 1000000), 0, -1):
        # 会津地鶏の代金
        cost_aizu = aizudori * c1
        if cost_aizu > b:
            continue
        # 残りの予算で普通の鶏肉を買う最大量
        max_normal_by_budget = (b - cost_aizu) // c2
        # 合計量がq1以上になるために必要な普通の鶏肉の量
        need_normal = max(0, q1 - aizudori)
        if max_normal_by_budget < need_normal:
            # 合計量を満たせない
            continue
        # 普通鶏肉は多く買うので、max_normal_by_budgetの範囲で買う。
        normal = max_normal_by_budget
        # q1以上の条件は保証されてるので答えにできる。
        ans_aizudori = aizudori
        ans_normal = normal
        break

    if ans_aizudori == -1:
        print("NA")
    else:
        print(ans_aizudori, ans_normal)