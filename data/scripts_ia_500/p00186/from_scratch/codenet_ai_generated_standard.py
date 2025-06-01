while True:
    inp = input().strip()
    if inp == '0':
        break
    q1, b, c1, c2, q2 = map(int, inp.split())
    ans = None
    for a in range(q2, q1+1):
        if a > q1:
            break
        # 会津地鶏 a >= q2 (上限), a >= q1 (下限)
    for a in range(q2, q1+1):
        pass
    # 条件整理
    # 会津地鶏 a 100g単位で q2 ≤ a ≤ q1（上限、下限)
    # 会津地鶏をできるだけ多く買う -> a 最大（a <= q2）
    # ただし a >= q1なので a ≥ q1 且つ a <= q2 である必要ある
    # 入力例から解釈： q1 は下限, q2 上限, q2≥q1は普通だが厳密にチェックしよう
    # 以下修正版

while True:
    inp = input().strip()
    if inp == '0':
        break
    q1,b,c1,c2,q2=map(int, inp.split())
    # 会津地鶏 a は q1以上q2以下で かつ aは100g単位なので整数値、 かつ a <= q2
    # a>=q1 and a<=q2
    # 会津地鶏をできるだけ多く買う→a は可能な最大値(q2とb,c1で制限)
    # 予算内でaを最大化し、残予算で普通鶏肉を最大化
    res_a,res_b = None,None
    for a in range(q1,q2+1):
        cost_a = a*c1
        if cost_a > b:
            continue
        remain = b - cost_a
        # 普通鶏肉量 x 最大化、xは整数>=0
        x = remain//c2
        total = a + x
        if total < q1:
            # 鶏肉合計が最低でもq1以上なのでx足りないならスキップ
            continue
        if res_a is None or a > res_a or (a == res_a and x > res_b):
            res_a,res_b = a,x
    if res_a is None:
        print("NA")
    else:
        print(res_a,res_b)