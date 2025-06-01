import sys
sys.setrecursionlimit(10**7)

def can_put(card, table):
    # カードが場に置けるか判定（場にあるカードの数字と連続しているか）
    if card == 7:
        return False
    if (card - 1) in table or (card + 1) in table:
        return True
    return False

def dfs(turn, first_cards, second_cards, table, memo):
    # メモによる枝刈り
    key = (tuple(sorted(first_cards)), tuple(sorted(second_cards)), turn, tuple(sorted(table)))
    if key in memo:
        return memo[key]

    if len(first_cards) == 0:
        # 先手が全部出したら勝ち
        memo[key] = True
        return True
    if len(second_cards) == 0:
        # 後手が全部出したら負け
        memo[key] = False
        return False

    if turn == 0:
        # 先手の番
        can_play = False
        for c in first_cards:
            if c == 7 or c - 1 in table or c + 1 in table:
                can_play = True
                new_table = table.copy()
                new_table.add(c)
                n_first = first_cards.copy()
                n_first.remove(c)
                if dfs(1, n_first, second_cards, new_table, memo):
                    memo[key] = True
                    return True
        if not can_play:
            # 出せない場合はパスして後手の番へ
            if dfs(1, first_cards, second_cards, table, memo):
                memo[key] = True
                return True
        memo[key] = False
        return False
    else:
        # 後手の番
        can_play = False
        for c in second_cards:
            if c == 7 or c - 1 in table or c + 1 in table:
                can_play = True
                new_table = table.copy()
                new_table.add(c)
                n_second = second_cards.copy()
                n_second.remove(c)
                # 後手はどのカードを出しても先手が勝てるならTrue
                if not dfs(0, first_cards, n_second, new_table, memo):
                    # 後手がこの出し方で負けないなら不利な展開あり
                    memo[key] = False
                    return False
        if not can_play:
            # 出せない場合はパスして先手の番へ
            if not dfs(0, first_cards, second_cards, table, memo):
                memo[key] = False
                return False
        memo[key] = True
        return True

N = int(input())
for _ in range(N):
    first = list(map(int, input().split()))
    # 7は場に置かれているので後手のカードは7以外で13枚から除いた6枚
    all_cards = set(range(1,14))
    all_cards.remove(7)
    first_set = set(first)
    second_set = all_cards - first_set
    table = {7}
    memo = {}
    if dfs(0, first_set, second_set, table, memo):
        print("yes")
    else:
        print("no")