# 坊主めくりのシミュレーション
# 入力のデータセットごとに、N人の参加者で札を順番に引いてルールに従って処理を行う
# 最終的に、各参加者が持つ札数を昇順に並べたものと、場に残る札の枚数を出力する

def bouzu_mekuri():
    while True:
        N = int(input())
        if N == 0:
            break  # 終了条件
        
        cards = input()
        
        # 各参加者の手札枚数リスト(要素は枚数の整数)
        players = [0] * N
        
        # 場にある札の枚数
        field = 0
        
        # 各参加者が持つ札の詳細（使わなくてもいいがデバッグ用に保持可）
        # 今回は枚数のみ追うので不要
        
        # 今回のルールでは、引いた札に応じて処理を行う
        # 男(M)：引いた人の手札に1枚追加
        # 坊主(S)：引いた人は自分の手札 + 引いた札をすべて場に出す。つまりその人の手札は0になり、場に増える。
        # 姫(L)：引いた人は引いた札 + 場にある全ての札をもらう。場の札は0になる。
        
        # 順番に札を引くのでi番目の札はi % N番目の人が引く
        for i, c in enumerate(cards):
            player = i % N
            
            if c == 'M':
                # 男札：引いた人に1枚追加
                players[player] += 1
            elif c == 'S':
                # 坊主札：引いた人は自身の札全て＋この札を場に出す
                # 自身の手札 + 1を場に移す
                field += players[player] + 1
                players[player] = 0
            elif c == 'L':
                # 姫札：引いた人は引いた札(1枚)と場にある札を全部もらう
                # 場の札は0になる
                players[player] += 1 + field
                field = 0
            else:
                # 予定外の文字の可能性はないが念のため
                pass
        
        # 出力は参加者の札数を昇順に並べ、その後に場の札枚数
        result = sorted(players)
        result.append(field)
        
        print(' '.join(str(x) for x in result))

if __name__ == "__main__":
    bouzu_mekuri()