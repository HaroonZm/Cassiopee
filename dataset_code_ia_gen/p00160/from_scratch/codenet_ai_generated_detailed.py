# 定義する宅配料金表
# サイズごとに「大きさ上限」「重さ上限」「料金」を対応づける
size_limits = [
    (60, 2, 600),
    (80, 5, 800),
    (100, 10, 1000),
    (120, 15, 1200),
    (140, 20, 1400),
    (160, 25, 1600),
]

def calculate_fee(x, y, h, w):
    """
    荷物の大きさと重さから料金を決定する関数。
    大きさは三辺の和。
    与えられた荷物がFサイズ（160cm以内かつ25kg以内）を超える場合は0を返す（対象外）。
    """
    size = x + y + h
    
    # サイズ順にチェックして、一番小さい適合サイズを選ぶ
    for size_limit, weight_limit, fee in size_limits:
        # 大きさも重さもそれぞれの上限以内ならこの料金
        if size <= size_limit and w <= weight_limit:
            return fee
    
    # サイズ上限もしくは重量制限を超えている場合は対象外（料金0）
    return 0

def main():
    import sys
    input = sys.stdin.readline

    while True:
        n_line = input()
        if not n_line:
            break
        n_line = n_line.strip()
        if n_line == '0':  # 入力終了条件
            break
        
        n = int(n_line)
        total_fee = 0
        for _ in range(n):
            line = input()
            x, y, h, w = map(int, line.strip().split())
            total_fee += calculate_fee(x, y, h, w)
        
        print(total_fee)

if __name__ == "__main__":
    main()