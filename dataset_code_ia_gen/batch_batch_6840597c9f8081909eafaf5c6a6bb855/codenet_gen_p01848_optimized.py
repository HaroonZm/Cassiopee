import sys
sys.setrecursionlimit(10**7)

def solve():
    input = sys.stdin.readline
    while True:
        N=int(input())
        if N==0:
            break
        p=[0]*N
        graph=[[] for _ in range(N)]
        for i in range(N):
            line=input().split()
            p[i]=float(line[0])
            m=int(line[1])
            if m>0:
                graph[i]=[int(x)-1 for x in line[2:]]

        # 枝の向きは「起きた人が連絡先に電話する」，
        # 起きた人は必ず連絡先を起こすため，
        # ある人が起きるためには，その人自身が起きるか，
        # もしくは自分に電話できる人(逆向きの辺の人)が起きている必要がある。
        # つまり逆向きにグラフを作り，連絡先から逆流できる人が全て起きている場合。
        # この集合で連絡可能な全員が起きる。
        # 起きる集合は連絡網の強連結成分で特徴づけられる。
        #
        # 各強連結成分をまとめて，そこに含まれる1人でも起きた(寝坊しなかった)人がいると
        # その成分の全員が起きる（モーニングコールで起こされるため）。
        #
        # 強連結成分の親グラフ(縮約グラフ)はDAGなので、トポロジカルに処理する。
        # 逆向きグラフで各人に電話できる人（つまりその人に入る辺）を把握して、その情報で成分を使う。
        #
        # これらから、強連結成分ごとに「少なくとも1人起きる確率」を
        # それぞれの成分の中のメンバーの起きる確率との関係でDPしていく。
        #
        # 方法：
        # 1. 強連結成分分解(SCC)
        # 2. 各SCCの成員の寝坊する確率p_iで「全員寝坊する確率」の積を計算→少なくとも1人起きる確率=1 - 積
        # 3. SCCの縮約グラフ（辺はSCC間の有向辺）
        # 4. DP：あるSCCが起きる確率
        #    SCCが起きる確率 = 1 - 確率(全員寝坊する) AND 確率(親SCC全て寝坊)
        #    ただしモーニングコールが来たら起きるので、
        #    SCCが起きるには、自分の成員の誰かが起きた or 親のSCCからモーニングコールが来る(親SCCが起きる)
        #    よって自分のSCCはその成員の起きる確率を使うが、親SCCは確率をDPで利用する
        #
        # 出発点は自分の成員の内「自分で起きる」人の起きる確率部分のみなので
        # 基本は親SCCの起きる確率に依存して増加する。
        #
        # トポ順に計算していく。
        #
        # 最後に全員が起きる=すべてのSCCが起きる
        # 全員起きる確率 = 後で計算したSCCの起きる確率をかけ合わせる。
        #
        # →ここで、「SCC内の人はみんな同時に起きる or 同時に寝坊する」ことになるので、
        # 寝坊の確率は「SCC内全員寝坊」の積を使い、起きるのは1-積。
        #
        # →しかしモーニングコールが伝播するため、
        #   最終的には「SCCが起きる確率」により全員起きるかが決まる。
        # →このDPは逆辺（倒しが入り口）に沿って起きる確率を更新
        #
        # まとめると、
        # - 強連結成分ごとに初期起きる確率s = 1 - ∏p_i（寝坊する確率）
        # - 縮約グラフで，親SCCが起きるとその子SCCも起きる(モーニングコール)
        # - 各SCCの起きる確率はs + (1-s) * (1 - ∏(1 - 親SCC起きる確率))
        # ただし親SCCからのモーニングコールを確率論的に合成し計算する。
        # これはトポロジカル順に起きる確率を計算する問題になる。
        #
        # 一般的にはトポソートしたSCC縮約グラフで、
        # scc起きる確率 dpは、
        # dp[SCC] = scc初期起きる確率 + (1 - scc初期起きる確率) * (1 - ∏ (1 - dp[parent]))
        #
        # dpは初期値0で、トポ順に更新する。ここはdp方程式の固定点問題かつ日常的ではない。
        #
        # 簡単にするため、逆に考えよう：
        #  各SCCが起きる確率は、
        #  1 - 寝坊する確率(全員寝坊) * ∏(親SCCが寝坊する確率)
        #
        # 寝坊する確率は「全員寝坊」= p_iの積。
        #
        # DPで親SCCが寝坊する確率を下流方向に掛けていく。
        #
        # つまり、
        # 起きる確率 = 1 - (SCC内全員寝坊の確率) * ∏(親SCCが寝坊する確率)
        #
        # これからトポロジカル順に「寝坊する確率」を
        # scc_sleep_prob[SCC] = (SCC内全員寝坊確率) * ∏(親SCCの寝坊確率)
        #
        # 先に親にモーニングコールが来なければそのSCCも寝坊確率はそのまま。
        #
        # SCC入辺(親)を記憶しよう。
        #
        # 最終的に全員起きる確率は∏(1 − scc_sleep_prob[scc])

        # 強連結成分分解
        order=[]
        used=[False]*N
        def dfs(v):
            used[v]=True
            for to in graph[v]:
                if not used[to]:
                    dfs(to)
            order.append(v)
        for i in range(N):
            if not used[i]:
                dfs(i)
        used=[False]*N
        comp=[-1]*N
        def rdfs(v,k):
            comp[v]=k
            used[v]=True
            for to in rev_graph[v]:
                if not used[to]:
                    rdfs(to,k)
        # 逆グラフを作成
        rev_graph=[[] for _ in range(N)]
        for i in range(N):
            for to in graph[i]:
                rev_graph[to].append(i)
        k=0
        for v in reversed(order):
            if not used[v]:
                rdfs(v,k)
                k+=1
        # kはSCC数

        # 各SCCのメンバーの寝坊確率の積(全員寝坊)
        scc_p=[1.0]*k
        for i in range(N):
            scc_p[comp[i]] *= p[i]

        # 縮約グラフ作成（逆グラフベースで親->子を保持）
        indeg=[0]*k
        scc_graph=[set() for _ in range(k)]
        # 入辺を親とする
        for i in range(N):
            for to in rev_graph[i]:
                ci=comp[i]
                cto=comp[to]
                if ci!=cto and cto not in scc_graph[ci]:
                    scc_graph[ci].add(cto)
        # scc_graph[i] は iの親SCCの集合（モーニングコールを送る先）
        # 逆向きにして親->子のグラフに直す（モーニングコールの伝播方向）
        # 今はscc_graph[i] = iの親SCC集合
        # モーニングコールは親から子へと伝播する（親が起きてると子を起こす）
        # つまり親SCC->子SCCなので、
        # ここは逆向きに直して、子リストscc_childrenを作る
        scc_children=[[] for _ in range(k)]
        indeg=[0]*k
        for i in range(k):
            for p_scc in scc_graph[i]:
                scc_children[p_scc].append(i)
                indeg[i]+=1

        from collections import deque
        # DP: scc_sleep_prob[i] = そのSCCが全員寝坊する確率（モーニングコールも無し）
        scc_sleep_prob = [0.0]*k
        # 初期値は各SCC内の全員寝坊確率
        for i in range(k):
            scc_sleep_prob[i] = scc_p[i]
        # トポロジカル順に更新
        q=deque([i for i in range(k) if indeg[i]==0])
        while q:
            u=q.popleft()
            for c in scc_children[u]:
                # cの寝坊確率 *= uが寝坊確率（u起きなければcはモーニングコール無しで寝坊が成り立つ）
                scc_sleep_prob[c]*=scc_sleep_prob[u]
                indeg[c]-=1
                if indeg[c]==0:
                    q.append(c)
        # 全員が起きる確率 = 1 - product of all scc_sleep_prob
        # ここではscc_sleep_probは「そのSCCが寝坊し続ける確率」
        # 起きる確率は 1-寝坊確率 なので、
        # しかしscc_sleep_probは「モーニングコール含めて寝坊する確率」の定義で計算済み（帰納的に）
        # 全体で「全員寝坊し続ける」のは ∏(SCC寝坊確率)ではない。この時点でscc_sleep_probは
        # 「モーニングコールが伝わった末の寝坊確率」になっているはずなので、
        # 個々のscc_sleep_probをかける必要はない。全部のメンバーは入っている。
        # 
        # 全員が寝坊し続ける確率は「全メンバーが寝坊し続ける」確率なので
        # = ∏p_i
        # だがp_iは独立で、モーニングコールで起きる場合の補正があるので、
        # dpでscc_sleep_probは「強連結成分がモーニングコールの影響受けずに寝坊する確率」まで寄せている。
        #
        # 実際にはSCC間の伝播をdpで掛けているので、
        # あるSCCにモーニングコールが来たらそのSCCは0になる（寝坊確率ゼロ）
        # 形をまとめると、
        # 全員が寝坊し続ける確率 = ∏ scc_sleep_prob[i]
        # なので全員が起きる確率 = 1 - ∏ scc_sleep_prob[i]
        ans = 1.0
        for sp in scc_sleep_prob:
            ans *= sp
        print(f"{1-ans:.9f}")

if __name__=="__main__":
    solve()