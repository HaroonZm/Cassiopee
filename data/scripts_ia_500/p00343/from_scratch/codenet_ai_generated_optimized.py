from sys import setrecursionlimit
setrecursionlimit(10**7)

def solve():
    N = int(input())
    all_cards = set(range(1,14))
    for _ in range(N):
        f_cards = set(map(int, input().split()))
        s_cards = all_cards - f_cards - {7}
        #場に7がある
        # f_cards,s_cardsは残り各6枚。7が場にある。
        # 盤の状態を左右拡張範囲で管理する
        # 左端,右端を7初期値にして、場のカードは場にある数字の集合
        # 各手番のプレイヤーが手持ちから数字を出すかパスかの繰り返しで終了条件はどちらかの手持ちが0になること
        # 後手が最善に出してきても先手が勝てる手順があるか（先手必勝か）
        #状態の定義: f_cards,s_cards,場の左端,右端,先手の番(Trueなら先手),手札は6枚以下なのでbitmaskで表現して高速化可能
        # 使用可能なカードは1..13除く7。
        #場の左端・右端は場に出たカードの最小・最大
        #場初期は7,左=7,右=7
        # 12枚全カード -7は 12枚 6先手・6後手

        #bitmaskで管理するためにカード-1をbitに対応させる(0-based index)
        # 7は場にあるため除外
        card_to_bit = {c: (1 << (c-1)) for c in range(1,14) if c != 7}
        bit_to_card = {v:k for k,v in card_to_bit.items()}
        #start masks
        f_mask = 0
        for c in f_cards:
            f_mask |= card_to_bit[c]
        s_mask = 0
        for c in s_cards:
            s_mask |= card_to_bit[c]
        left = 7
        right = 7
        from functools import lru_cache

        @lru_cache(None)
        def dfs(fm,sm,l,r,turn): # turn=True:先手,False:後手
            #終了条件
            if fm == 0:
                return True #先手勝ち
            if sm == 0:
                return False #後手勝ち(先手敗北)
            #次のカードの候補場に置けるかを見る
            #左端より1小さいか右端より1大きいカードを持っていれば必ず出す
            #複数あれば好きなものを選べる
            #順番に全部試す -> 先手番なら1つでもTrueならTrue,後手番なら1つでもFalseならFalse
            #手札配布6枚は少ないので深さ優先でも十分
            #探せるカード
            if turn:
                hand = fm
            else:
                hand = sm

            candidates = []
            left_card = l-1
            right_card = r+1
            if left_card >= 1 and (hand & card_to_bit.get(left_card,0)):
                candidates.append(left_card)
            if right_card <= 13 and (hand & card_to_bit.get(right_card,0)):
                candidates.append(right_card)

            if candidates:
                #出せるカードがある場合出さなければならない
                # 先手なら一つでもTrueがあればTrue
                # 後手なら一つでもFalseがあればFalse
                if turn: #先手番
                    for c in candidates:
                        new_fm = fm & ~card_to_bit[c]
                        new_l = min(l,c)
                        new_r = max(r,c)
                        if dfs(new_fm, sm, new_l, new_r, False):
                            return True
                    return False
                else: #後手番
                    for c in candidates:
                        new_sm = sm & ~card_to_bit[c]
                        new_l = min(l,c)
                        new_r = max(r,c)
                        # 後手が勝つ手順を一つでも見つけたら先手敗北
                        if not dfs(fm, new_sm, new_l, new_r, True):
                            return False
                    return True
            else:
                #出せるカードがない場合はパスして相手の番
                return dfs(fm, sm, l, r, not turn)

        print("yes" if dfs(f_mask,s_mask,left,right,True) else "no")

if __name__ == "__main__":
    solve()