# 解法アプローチ：
# 1. 入力からN（競技者数）、M（優勝した競技者の番号）、P（控除率）を読み取る。
# 2. N人分の投票数X_iを読み取る。
# 3. すべての投票数の合計を計算し、これに100ゴールドを掛けてトータルの掛け金総額を得る。
# 4. 控除金額を差し引いた後の配当金プールを計算する。（控除は百分率Pで計算し、小数点以下は切り捨て）
# 5. 優勝者Mに掛けられた投票券の数を取得し、これが0なら0を出力。
# 6. 配当金プールを優勝者の投票券枚数で割り、1枚あたりの配当金を整数で切り捨てる。
# 7. 各データセットについて上記を繰り返し出力する。
#
# 注意：
# 出力は数字のみで余計な文字を入れない。
# 入力終端は「0 0 0」の行で判定する。

while True:
    # 入力行を読み込み、空白区切りで整数に変換
    line = input().strip()
    if line == '0 0 0':
        break
    N, M, P = map(int, line.split())
    votes = []
    for _ in range(N):
        x = int(input().strip())
        votes.append(x)
    
    total_tickets = sum(votes)         # 総投票券数
    total_gold = total_tickets * 100   # 総ゴールド掛け金
    
    # 控除後の賞金プールを計算（P%控除、切り捨て）
    pool = total_gold * (100 - P) // 100
    
    winning_tickets = votes[M - 1]     # 優勝者の投票券数
    
    if winning_tickets == 0:
        print(0)
    else:
        payout_per_ticket = pool // winning_tickets
        print(payout_per_ticket)