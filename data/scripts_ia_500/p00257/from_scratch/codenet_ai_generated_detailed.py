# すごろくの盤面を考える。  
# 「ふりだし」を0、「あがり」をn+1とし、間のマスを1～nとする。  
# 各マスに指示があり、指示に従って進む・戻る。  
# ルーレットは1～maxの値を等確率で出すが、ここでは最悪の場合を判定するため、どの値も出る可能性があると考える。  
# 「あがり」にたどり着けない場合＝盤面のどこかに永遠に抜け出せない閉路（不動点あるいは閉じた移動のループ）がある場合。  
# この盤面で、次のステップはルーレットの任意の出目のどれかで「あがり」に行けるか、または閉じ込められるかの判定問題。  

# 解法方針：  
# 各マス i(0～n+1) から、ルーレットの出目 r(1～max) を足して一旦右に進み、その後指示に従って移動する。  
# 指示によりあふれたら「ふりだし」または「あがり」に丸める。  
# この動きを「1手の遷移」としてグラフを作る。

# 重要な条件は、「指示に従って移動した先のマスの指示には従わない」（つまり指示は1回のみ適用）

# 全ての遷移を作り、状態遷移グラフとして扱うと、複数の遷移先がある（ルーレットの出目が複数ある）ため非決定性グラフに近いが、ここは「どの出目も起こりえる」ので  
# 「すべての遷移が『あがりにたどり着ける』方向に向いている」かを判定する必要がある。  
# つまり、「どの出目が出ても最終的にあがりにたどり着く」ならOK、そうでなければNG。  

# 問題文より、「どの出目でも～」という解釈ではなく、「どの出目により～」なので、いずれかの出目の選択によりあがりにたどり着けないケースがあるとNG。  
# 入力例からもそう判断できる。  
# つまり、  
# 「すべてのマスから、どの出目をとっても、必ずあがりに到達できる」→ OK  
# 「存在するマスからのある出目の遷移先が、永久にあがりに達しない閉路に入る可能性がある」→ NG  

# アルゴリズム：  
# 1. 各マスiから、すべての出目rについて、遷移先jump(i,r)を計算する（指示適用後のマス番号）  
# 2. 「あがり」マス= n+1 を終点とする  
# 3. あがりに到達できるマスを逆方向グラフで探索し、あがりに到達可能なマス集合を求める  
# 4. すべての遷移の遷移先があがりに到達可能でなければならない。  
# 5. 一つでも遷移先があがりに到達不可の遷移が存在すればNG  

# 実装のポイント  
# - 入力の指示は n行、マス番号は 1～n, 0がふりだし、n+1があがり  
# - jump(i, r) = i + r でいったん移動し、はみだした場合はあがりへ  
# - 指示適用後の移動先も同様にはみだした場合はあがり  
# - 指示の戻りがふりだしより前ならふりだしに戻る  
# - 指示は1回しか適用しない  

import sys
sys.setrecursionlimit(10**7)

def solve():
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        max_r = int(line.strip())
        if max_r == 0:
            break
        n = int(sys.stdin.readline().strip())
        d = []
        for _ in range(n):
            d.append(int(sys.stdin.readline().strip()))
        # マス番号: 0=ふりだし, 1～n, n+1=あがり
        start = 0
        goal = n+1

        # jump(i, r) を計算する関数
        # i=0..n+1, r=1..max_r
        # 最初に i+r で移動し、次にそのマスの指示を適用。ただし指示は一回のみ適用。
        # 指示により範囲からあふれたら start or goal に丸める
        # 指示が無い（d=0）はそのままそのマスに止まる

        # d のインデックスは 0-based でマス1に対応するので、d[i-1]がマスiの指示
        def jump(i, r):
            if i == goal:
                return goal  # 既にあがり
            pos = i + r
            if pos >= goal:  # 行き過ぎたらあがりへ
                return goal
            # 指示を適用
            di = d[pos-1]  # マス番号 pos の指示
            if di == 0:
                return pos
            next_pos = pos + di
            # 範囲チェック
            if next_pos < start:
                return start
            if next_pos > goal:
                return goal
            return next_pos

        # 状態数は n+2（0〜n+1）
        # グラフの辺を作る（状態 -> すべての jump(i,r)）
        # あがりに到達可能か逆方向グラフで判定
        edges = [[] for _ in range(goal+1)]  # 逆辺グラフ： 到達元を保持
        outdeg = [0]*(goal+1)  # 順辺の数を数える（以降利用しないが念のため）

        for i in range(goal+1):
            for r in range(1, max_r+1):
                nxt = jump(i, r)
                outdeg[i] += 1
                edges[nxt].append(i)  # 逆辺

        # あがりが終端状態となる。あがりから逆方向探索で
        # あがりに到達できるマスを調査
        from collections import deque
        reachable = [False]*(goal+1)
        q = deque()
        reachable[goal] = True
        q.append(goal)

        while q:
            cur = q.popleft()
            for prev in edges[cur]:
                if not reachable[prev]:
                    reachable[prev] = True
                    q.append(prev)

        # すべてのマス i のすべての遷移先 jump(i,r) が reachableなら OK
        # そうでない遷移先があれば NG

        res = "OK"
        for i in range(goal+1):
            for r in range(1, max_r+1):
                nxt = jump(i, r)
                if not reachable[nxt]:
                    # 到達できない遷移あり
                    res = "NG"
                    break
            if res == "NG":
                break

        print(res)

if __name__ == "__main__":
    solve()