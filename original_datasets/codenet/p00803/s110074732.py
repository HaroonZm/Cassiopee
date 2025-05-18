ans = [] # 答え
while True:
    N = int(input())
    if not N:
        break
    
    now_cube = int(N ** (1 / 3 + 0.000001))
    now_pyramid = 0
    tmp_ans = now_cube ** 3
    
    # 立方体の一辺を小さくしていく、立方体の辺ごとに四角錐の一辺の長さを求め、容量を求める
    for i in range(now_cube, -1, -1):
        while True:
            # もし次の値が最大容量を超えるならば
            if (now_pyramid + 1) * (now_pyramid + 2) * (now_pyramid + 3) // 6 + i ** 3 > N:
                # 超えない値の時にこれまでの最大値と比較して大きい方を答えとする
                tmp_ans = max(tmp_ans, now_pyramid * (now_pyramid + 1) * (now_pyramid + 2) // 6 + i ** 3)
                break
                
            # 四角錐の一辺を大きくしていく
            now_pyramid += 1
    
    ans.append(tmp_ans)
    
# 出力     
[print(i) for i in ans]