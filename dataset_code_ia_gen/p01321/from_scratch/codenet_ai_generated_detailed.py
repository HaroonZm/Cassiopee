while True:
    n = int(input())
    if n == 0:
        break  # 入力の終わり
    
    max_score = -1   # 最高点の初期化（0点未満はありえないので-1で十分）
    min_score = 501  # 最低点の初期化（最高は500点なので501で初期化）
    
    for _ in range(n):
        scores = list(map(int, input().split()))
        total = sum(scores)  # 5教科の合計点を計算
        if total > max_score:
            max_score = total
        if total < min_score:
            min_score = total
    
    print(max_score, min_score)  # 最高点と最低点を1文字の空白で区切って出力