# 解説：
# ゲームのルールに従い、太郎と花子の両方が「出せるカードのうち最小のものを必ず出す」戦略でカードを出す。
# 一方の手札が無くなるまでゲームを進める。
# パスした場合、場のカードはリセットされる。
# 入力は複数データセットでn=0で終了。
# 出力は各データセットごとに2行、太郎と花子の得点（相手の残りカード枚数）を表示。

import sys

def simulate_game(n, taro_cards):
    # 1〜2nのカード。太郎のカードが与えられる。花子のカードはそれ以外。
    all_cards = set(range(1, 2*n+1))
    hanako_cards = sorted(all_cards - set(taro_cards))
    taro_cards = sorted(taro_cards)

    # 手札をリストの形で持つ
    # プレイヤーの番を管理: True=太郎, False=花子
    # 各プレイヤーは手札中で出せるカードの一番小さいものを出す
    # 場に出ているカードを管理、初期はNone（場が空）
    field = None

    # 手札はリストなので、カードを出す際はpop(0)的に先頭から使うイメージ
    # しかしルールは「出せるカードのうち最小を出す」
    # 取り出し戦略に合わせて、リストはソート済みなので左から順に見る
    # 使えるカードがなければパス→場リセット→相手番へ

    # 手札をリストで管理し、カード使用時は削除
    # カードを出す関数（手札リスト, 場のカード)→出せる最小カードの番号 or None
    def find_card_to_play(hand, field_card):
        # 場にカードが無いなら好きなカード（最小）を出せる
        if field_card is None:
            return hand[0]
        else:
            # last_cardより大きい手札の最小カードを探す
            for c in hand:
                if c > field_card:
                    return c
            # 見つからなければ出せない
            return None

    # 手札はリスト、カードを出す度に削除
    taro_hand = taro_cards[:]
    hanako_hand = hanako_cards[:]

    turn_taro = True  # Trueなら太郎の番
    while len(taro_hand) > 0 and len(hanako_hand) > 0:
        if turn_taro:
            card_to_play = find_card_to_play(taro_hand, field)
            if card_to_play is None:
                # パス→場リセット
                field = None
                turn_taro = False
            else:
                # 出せる最小カードを出す
                taro_hand.remove(card_to_play)
                field = card_to_play
                turn_taro = False
        else:
            card_to_play = find_card_to_play(hanako_hand, field)
            if card_to_play is None:
                field = None
                turn_taro = True
            else:
                hanako_hand.remove(card_to_play)
                field = card_to_play
                turn_taro = True

    # ゲーム終了時に得点を出力
    # 太郎の得点＝花子の残り枚数
    # 花子の得点＝太郎の残り枚数
    print(len(hanako_hand))
    print(len(taro_hand))

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = int(input_lines[idx])
        idx += 1
        if n == 0:
            break
        taro_cards = []
        for _ in range(n):
            taro_cards.append(int(input_lines[idx]))
            idx += 1
        simulate_game(n, taro_cards)

if __name__ == "__main__":
    main()