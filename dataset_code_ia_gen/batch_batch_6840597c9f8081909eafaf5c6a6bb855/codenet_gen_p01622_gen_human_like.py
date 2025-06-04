import sys

def solve():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        books = [tuple(map(int, input().split())) for _ in range(N)]

        # まず読む時間の合計を最小にすることが条件なので
        # すべての本の読む時間をどう割り振っても合計は固定
        # 双子の読む時間は最大の読む時間の合計（最大完了時間）を最小化したい
        # 本は読む→感想文を書く順固定。
        # 読み終わり時間 = max(読了アミ, 読了マミ)
        # 宿題終了時間 = max(終了アミ, 終了マミ)

        # 読む作業は各本1回ずつ同時にできないので、
        # 読む時間の分割問題となり、双子に本を割り振って読む合計時間の最大値を最小化する問題。
        # つまり、r_iのうち片方には読むa_i読、もう片方b_i読むの割り振り最適化問題(パーティション問題)。

        # 読み終わり時間の最小を求めるのは、
        # 読む時間r_iを2グループに分け、各グループの合計がなるべく近くなるようにすること。

        # つまり、読む時間のリストr_iについて、
        # r_iの部分集合和pを決めて、
        # 読み終わり時間をmax(p, sum(r_i) - p)
        # が最小になるpを探す（部分和問題）
        # このpで読み終わり時間最小確定。

        # 次にこの振り分けに対して感想文の書く順番を決める。
        # 感想文の感想文書き時間w_iは読む時間完了後に書く。

        # 感想文書きは読む作業終了後に書く。
        # 書く作業が並列できないことはないので、
        # 書く時間の並列は同じ読み終わり時間のタイムスタンプから並べて行ける。

        # しかし、問題文を見ると読むと感想文書きを同時にできるかは明確でない。
        # 読む・書くは同時にできる（そう解釈するのが自然）。
        # 読むは1冊ずつしかできず中断できないが、書くは中断不可だが空き時間は有効利用できる。
        # 従って、書く順序で終了時間を短縮できる。
        # 2人は読書・感想文執筆自体は別プロセスなので、それぞれの作業を別々に処理できる。

        # まとめ：
        # 読むは本人ごとに割り振って時刻積算、
        # 書くは読む完了順に処理し、その人の書き手のタイミングの最新時間から書き始める。

        # 重要なことは読む時間のパーティションを求めて、読む時間の最大最小化

        total_r = sum(r for r, w in books)
        max_r = max(r for r, w in books)

        # dpで部分和問題を解く
        max_sum = total_r
        half = total_r // 2

        dp = [False] * (half + 1)
        dp[0] = True

        for r, w in books:
            for s in range(half, r - 1, -1):
                if dp[s - r]:
                    dp[s] = True

        # 読み終わり時間最小はmax(読み割り振り時間)
        # dpでsでTrueな最も大きいsを探す
        for s in range(half, -1, -1):
            if dp[s]:
                # 読み終わり時間 = max(s, total_r - s)
                read_end = max(s, total_r - s)
                break

        # 2人の読む割り振り時間はs, total_r - sの２グループ

        # 本をどちらが読むかを決めるための復元作業
        # 本の割り振り方法(どっちが読むか)が必要
        # dpの復元は重いがN<=1000でr_i<=1000で可能

        # 復元用に各本とdp配列保存
        dp2 = [set() for _ in range(N+1)]
        dp2[0].add(0)
        for i in range(N):
            r = books[i][0]
            new_set = set()
            for val in dp2[i]:
                new_set.add(val)
                if val + r <= half:
                    new_set.add(val + r)
            dp2[i+1] = new_set

        # sはdpにある最適な部分和
        # sに近い値で決めた
        # ここでsを使って復元
        selected = [False] * N
        cur = s
        for i in range(N-1, -1, -1):
            r = books[i][0]
            if cur - r in dp2[i] :
                selected[i] = True
                cur -= r
            # else False, i番目は選ばれなかった

        # selected[i] = Trueの本はアミが読むとする（読む合計s）
        # Falseの本はマミ

        # それぞれの読むスケジュール(時刻累積)
        ami_read_end = 0
        mami_read_end = 0
        # 読み終わり時間はread_endで最小として決まっているのでここはとりあえず順序で積んでいく

        # 感想文を書く完了時刻を計算する
        # 感想文は読む終了後順に書き始めるため
        # 感想文は本人毎に並列できないので、その本人の感想文完了時間を管理する。

        # それぞれの本人が読む順序決める。読む中断不可→順番を何にするか？
        # 感想文書き時間を最小化するには、
        # 読み終わった順に感想文を書くので、感想文書きを短くするためには
        # 読書終わり時間最小の割り振りは決定したあと、本の読む順番を決める必要あり

        # 読む順番はそれぞれのグループの本の並び替えで感想文書き終了時間を最小化
        # ジョブスケジューリングの基本　読む時間は固定割り振り、感想文は書き時間のみで終了時間最小化

        # 読む時間は固定割り振りでそれぞれの順番で積み重ねるため、読む開始時間が決まる
        # そのため、書き時間の開始時間 = 読む終了時間のあと本人の感想文完了時刻（前回の感想文完了時刻）

        # 感想文書きの順番で終了時間が変わる。
        # ここでジョンソンのルール風に考えると、
        # 読む時間と書く時間は分離されているので、
        # 書く時間だけ本人の処理順序で決定

        # しかし読む開始順番で良いのは読書完了時間の早い順に書くことで終了時間を減らせるので
        # 本の読む順番も感想文書き終了時間に影響する
        # 
        # 感想文書き完了時間の最小化のためには、
        # 本の読む順番を感想文書き時間の大小順にすることが良い
        # 感想文書きが長いものを先に読むことで、その後の感想文書きが遅れるのを防ぐイメージ
        # ただし読む割り振りの時間の和は変わらないため厳密には少し複雑

        # ここでは読む順序は感想文の書き時間の降順にしてみる。

        ami_books = []
        mami_books = []
        for i in range(N):
            if selected[i]:
                ami_books.append(books[i])
            else:
                mami_books.append(books[i])

        # 感想文書き時間の降順にソート
        ami_books.sort(key=lambda x: x[1], reverse=True)
        mami_books.sort(key=lambda x: x[1], reverse=True)

        def compute_finish_time(books):
            time_read = 0
            time_write_end = 0
            for r, w in books:
                time_read += r
                # 感想文は読書完了後、感想文作業が終わっていればすぐ開始できる
                time_write_start = max(time_read, time_write_end)
                time_write_end = time_write_start + w
            return time_write_end

        ami_end = compute_finish_time(ami_books)
        mami_end = compute_finish_time(mami_books)

        print(max(ami_end, mami_end))


if __name__ == "__main__":
    solve()