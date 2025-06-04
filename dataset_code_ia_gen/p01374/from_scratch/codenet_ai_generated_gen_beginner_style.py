import sys
sys.setrecursionlimit(10**7)

MOD = 1000000007

def build_AC_automaton(patterns):
    # Trieノード構造
    # nodes[i]: {char: next_node, ...}
    # fail[i]: fail link
    # output[i]: 季語IDのビット集合（0ならなし）
    nodes = [{}]
    fail = [0]
    output = [0]

    for idx, pat in enumerate(patterns):
        current = 0
        for c in pat:
            if c not in nodes[current]:
                nodes[current][c] = len(nodes)
                nodes.append({})
                fail.append(0)
                output.append(0)
            current = nodes[current][c]
        output[current] |= (1 << idx)

    # fail構築（BFS）
    from collections import deque
    queue = deque()
    for c, nxt in nodes[0].items():
        queue.append(nxt)
    while queue:
        r = queue.popleft()
        for c, nxt in nodes[r].items():
            queue.append(nxt)
            f = fail[r]
            while f > 0 and c not in nodes[f]:
                f = fail[f]
            fail_nxt = nodes[f][c] if c in nodes[f] else 0
            fail[nxt] = fail_nxt
            output[nxt] |= output[fail_nxt]
    return nodes, fail, output

def main():
    input = sys.stdin.readline

    while True:
        N, M, K = map(int, input().split())
        if N == 0 and M == 0 and K == 0:
            break

        edges = []
        words_set = set()
        for _ in range(N):
            f, t = input().strip().split()
            edges.append((f, t))
            words_set.add(f)
            words_set.add(t)

        season_words = [input().strip() for _ in range(K)]

        # 単語リストとID割り当て
        words = list(words_set)
        words.sort()
        w2i = {w:i for i,w in enumerate(words)}

        # 接続辞書の隣接リスト
        adj = [[] for _ in range(len(words))]
        for f,t in edges:
            adj[w2i[f]].append(w2i[t])

        # 季語をACオートマトン構築のパターンにする
        # ただし季語は文章中単語の境界をまたいで出現してよい
        # なので単純に単語を連結した文字列を考えて部分文字列として季語を探す
        # => 各単語を文字列として扱い、その連結が対象

        # ACオートマトン構築（季語パターン）
        ac_nodes, ac_fail, ac_out = build_AC_automaton(season_words)

        ac_size = len(ac_nodes)

        # dp[pos][word][ac_state][season_mask]
        # => pos: 何単語目か (1~M)
        # season_mask: 季語のどれかが1回出現したかのビット管理。0=なし, 1<<k=k番目季語検出済み
        # だが季語が複数出現はダメ、複数種類もダメ。つまりseason_maskは0か1bitだけ立っている状態のみ許される
        # 季語が2回出現以上はダメ。そうすると季語が見えた時印をつけ、2回目以降とか2種目とかは弾く
        # 到達不可能な状態は0。

        # メモリ削減のため
        dp = [[[0]*(1<<K) for _ in range(ac_size)] for _ in range(len(words))]
        # 初期状態：詩は単語0回だけ。だが詩は最初の単語から始めて作るので実際は1単語目の単語各位置から数える
        # 問題文「詩は接続辞書に含まれるどの単語から始めてもよい」
        # よって1単語目は任意の単語でよい

        for w in range(len(words)):
            # 初期は単語をまだつなげていないからpos=1の状態にする
            # 初期状態として単語wの文字列からACオートマトンを流す必要あり
            # ここで季語検出もあるのでACオートマトン遷移を手続き的に行う

            s = words[w]
            state = 0
            mask = 0
            for c in s:
                while state > 0 and c not in ac_nodes[state]:
                    state = ac_fail[state]
                if c in ac_nodes[state]:
                    state = ac_nodes[state][c]
                else:
                    state = 0
                mask |= ac_out[state]

            # maskには複数ビット立つ可能性ありだが詩条件としては複数出たらダメ(詩全体で季語は一度だけ)
            # 初期単語ひとつで複数季語同時はないはず、K<=30でも問題の季語は1文字以上20文字以下の英字で異なっている
            # 念のため、複数季語検出＝アウト
            if mask == 0 or (mask & (mask - 1)) == 0:
                dp[w][state][mask] = (dp[w][state][mask] + 1) % MOD

        for pos in range(1, M):
            ndp = [[[0]*(1<<K) for _ in range(ac_size)] for _ in range(len(words))]
            for w in range(len(words)):
                for st in range(ac_size):
                    for msk in range(1<<K):
                        cur = dp[w][st][msk]
                        if cur == 0:
                            continue
                        # 次の単語へ遷移
                        for nxt in adj[w]:
                            s = words[nxt]
                            state = st
                            mask = msk
                            # 文字列をACに流す
                            for c in s:
                                while state > 0 and c not in ac_nodes[state]:
                                    state = ac_fail[state]
                                if c in ac_nodes[state]:
                                    state = ac_nodes[state][c]
                                else:
                                    state = 0
                                mask |= ac_out[state]
                            # maskは詩中に存在する季語集合。問題は一度だけの1単語長目詩中ならOK
                            # 複数季語出現or同一季語2回以上出たらNG:
                            # maskにあるビットが1個だけか0でないと成立しない
                            # dp状態で初期maskが0で、maskが新たに複数ビット増えた場合はNG
                            # ただしmaskは全体の季語集合
                            # 新たに季語が増えたり重複したらNG
                            # 以下の判定は
                            # - 0ならまだ季語無しなのでOK
                            # - 1 bitだけ立ってるのもOK
                            # - 2 bit以上立ってるのはNG

                            # maskはdp更新前のmskに新たに季語出現部分をORで加えたもの
                            # 複数季語でることや２度目の同じ季語もmaskのビット数で判断可能。
                            # ただしmaskだけでは2度目の季語出現は見えないため
                            # 季語出現は文章連結で跨るため単純ビットかけ算で重複もわかる。ACオートは重複したらアウト
                            # 複数bitが立つ≒2種類以上出現

                            # mask内の1bit数チェック
                            if mask == 0:
                                ndp[nxt][state][mask] = (ndp[nxt][state][mask] + cur) % MOD
                            elif (mask & (mask - 1)) == 0:
                                # 季語１つだけなのでOK
                                ndp[nxt][state][mask] = (ndp[nxt][state][mask] + cur) % MOD
                            # else 複数bit立ってる場合はNG（スルー）

            dp = ndp

        # pos = Mとなったら、季語が1つだけ出ている状態を数える
        ans = 0
        for w in range(len(words)):
            for st in range(ac_size):
                for msk in range(1<<K):
                    # 季語は1個だけ出ている状態のみ許す
                    if (msk & (msk - 1)) == 0 and msk != 0:
                        ans = (ans + dp[w][st][msk]) % MOD

        print(ans)

if __name__ == "__main__":
    main()