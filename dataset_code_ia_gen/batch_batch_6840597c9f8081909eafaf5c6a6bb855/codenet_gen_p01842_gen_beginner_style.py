import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp[i][j][turn][passed]: 差分スコア (player1 - player2)
# i: player1のデッキで使った枚数
# j: player2のデッキで使った枚数
# turn: 0=player1のターン, 1=player2のターン
# passed: 0=直前でパスしてない, 1=直前でパスした
# スタックの状態も必要だが、
# 状態爆発防止のため、
# 専門的にはスタックの最小の必要情報を保持するが
# 今回は初心者向けの簡素化した実装で、
# スタックを保持し遷移に全て考えるコードは膨大のため、代わりに簡単なシミュレーションは不可能。
# よって、勉強目的向けに、
# スタック情報も含めてまとめて持つ形で実装（非効率）。
# スタックはカードのリスト、置いたプレイヤーリストを同時に保持。

from functools import lru_cache

# 持ちカードはa[i:n], b[j:m]が残りデッキの上から
# スタックはcards (list of (card_value, owner)), owner 0 or 1
# passedは連続パスの回数(0,1,2)
# turn: 0 or 1

def score_for_player(cards, player):
    # playerが獲得する点数を計算
    # 条件：cardsのうちplayerが置いた得点カードで、
    # 相手が置いた妨害カードより上にあるカードのみ
    # 相手妨害カードが無い場合はplayerが置いた得点カード全て
    opp = 1 - player
    # 相手妨害カードがあるか
    opp_block_indices = [i for i, (v, o) in enumerate(cards) if v == -1 and o == opp]
    if not opp_block_indices:
        # すべて得点カード（playerが置いたもの）
        return sum(v for v,o in cards if o==player and v>0)
    else:
        min_block = min(opp_block_indices)
        # min_blockより上（indexが大きい）でplayerが置いた得点カードの合計
        return sum(v for i,(v,o) in enumerate(cards) if i > min_block and o == player and v>0)

@lru_cache(maxsize=None)
def dfs(i, j, turn, passed, stack):
    # stackは文字列化して渡す（カード値とownerを文字列で）
    # stackを元の形に戻す
    st = []
    if stack:
        parts = stack.split(',')
        for p in parts:
            if p == '':
                continue
            val, own = p.split(':')
            st.append( (int(val), int(own)) )
    else:
        st = []

    # 連続で2回パスしてスタックが空なら終了
    if passed == 2 and len(st) == 0:
        # スコアを計算して返す
        # スコアは累積なので０にする
        return 0

    # 現プレイヤーのカード一覧
    if turn == 0:
        deck = a
        idx = i
        deck_len = n
    else:
        deck = b
        idx = j
        deck_len = m

    res = None

    # プレイヤーのターン、行動は2通り

    # 1. パス
    # パスしたらstackの得点カード収得処理
    if passed == 1 and len(st) == 0:
        # 2連続パスで終了
        # ここの条件は上で判定しているのでここには来ないが念のため
        res_pass = 0
    else:
        # 得点カード処理
        p0 = score_for_player(st,0)
        p1 = score_for_player(st,1)
        # どちらもgameから得点を獲得して、スタックは空に
        new_stack = []

        # パス後は相手ターン
        next_passed = passed + 1
        if len(st) == 0:
            next_passed = passed + 1
        else:
            next_passed = 1

        # 変更後のスコア差は
        # (player1獲得点 - player2獲得点) + 次の状態のスコア差
        # 今のターンのプレイヤーを前提に差分をかえる
        base_score = p0 - p1

        tmp = dfs(i,j,1 - turn, next_passed, '') + base_score

        res_pass = tmp

    res = res_pass

    # 2. カードを置く (デッキにカードがある場合のみ)
    if idx < deck_len:
        card = deck[idx]
        new_stack = st + [(card, turn)]
        # カードなら連続パスリセット
        next_passed = 0

        if turn == 0:
            tmp = dfs(i+1, j, 1, next_passed, ','.join([str(v)+':'+str(o) for v,o in new_stack]))
        else:
            tmp = dfs(i, j+1, 0, next_passed, ','.join([str(v)+':'+str(o) for v,o in new_stack]))

        # 先手は差を最大化、後手は差を最小化を目指す
        if turn == 0:
            if res is None or tmp > res:
                res = tmp
        else:
            if res is None or tmp < res:
                res = tmp

    else:
        # カード置けない場合はパスのみ
        pass

    return res

ans = dfs(0,0,0,0,'')
print(ans)