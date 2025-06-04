# 宝くじチェッカー問題の解法を示します。
# 入力で複数データセットが与えられ、n=0,m=0で終了です。
# 当選番号は8桁で数字と'*'が混在し、宝くじ番号とマッチするかを判定します。
# 1枚の宝くじは複数の当選番号に重複当選しないため、全て独立に加算できます。

def match(lottery_num: str, winning_pattern: str) -> bool:
    """
    宝くじ番号と当選パターンがマッチするか判定する関数。
    winning_pattern は数字か'*'で8桁。
    '*'はどの数字でもマッチ。
    """
    for i in range(8):
        if winning_pattern[i] != '*' and winning_pattern[i] != lottery_num[i]:
            return False
    return True

def main():
    import sys

    # 複数データセットを読み込む
    for line in sys.stdin:
        if not line.strip():
            continue
        # n,mを取得
        n_m = line.strip().split()
        if len(n_m) < 2:
            # 入力不足行なら次へ
            continue
        n, m = map(int, n_m)
        if n == 0 and m == 0:
            # 終了判定
            break

        winning_patterns = []
        # 当選番号と当選金をn行読む
        for _ in range(n):
            w_line = sys.stdin.readline().strip()
            pattern, prize = w_line.split()
            prize = int(prize)
            winning_patterns.append((pattern, prize))
        
        lottery_nums = []
        # 所持宝くじ番号をm行読む
        for _ in range(m):
            l_line = sys.stdin.readline().strip()
            lottery_nums.append(l_line)
        
        total_prize = 0
        # すべての宝くじについてすべての当選番号と照合
        # 複数当選番号に該当しないので1宝くじ1当選番号以下で、重複当選はない
        # よって単純に合致する当選番号の賞金を加算すればよい
        for num in lottery_nums:
            for pattern, prize in winning_patterns:
                if match(num, pattern):
                    total_prize += prize
                    # 問題文の条件から1宝くじが2つ以上に当選しないためここでbreakでもOK
                    break
        
        print(total_prize)

if __name__ == "__main__":
    main()