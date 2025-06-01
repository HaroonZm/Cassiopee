# 元金を100として計算を行う
# 各データセットごとに最も元利が大きい銀行番号を出力する

while True:
    n = int(input())  # 銀行の数
    if n == 0:
        break  # 入力終了
    
    y = int(input())  # 預ける年数
    max_total = -1  # 最大元利の初期化
    max_bank = None  # 最大元利の銀行番号
    
    for _ in range(n):
        b, r, t = map(int, input().split())
        principal = 100  # 元金は100と仮定
        
        if t == 1:
            # 単利の場合: 元利 = 元金 + (元金 * 年利率/100 * 年数)
            total = principal + principal * r / 100 * y
        else:
            # 複利の場合: 元利 = 元金 * (1 + 年利率/100)^年数
            total = principal * ((1 + r / 100) ** y)
        
        # 最大元利を更新
        if total > max_total:
            max_total = total
            max_bank = b
    
    print(max_bank)