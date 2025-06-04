import sys
import math

def solve():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        books = [tuple(map(int, input().split())) for _ in range(N)]
        # 各本の (r, w)
        # 問題の条件を考慮しないといけない
        # まず2人で本を分散して読むため読む時間は「全本の合計時間の半分の天井以上」になる
        total_r = sum(r for r, w in books)
        left = math.ceil(total_r / 2)
        right = total_r

        # 判定関数：読み終わる時間tで、2人が読み終えるまでに両者の読む時間分配可能か
        # 判定できれば、そのt以内に読める分割がありうる
        def can(t):
            # 2人の最大読み時間はt
            # 両者合計はtotal_rなのでt >= ceil(total_r/2)
            # dp[i][j]: i冊目までで、一人がj時間まで読めるか(ブール)
            dp = [False]*(t+1)
            dp[0] = True
            for r, _ in books:
                newdp = [False]*(t+1)
                for j in range(t+1):
                    if not dp[j]:
                        continue
                    # 一人がj時間読むとき
                    if j + r <= t:
                        newdp[j+r] = True
                    if r <= t:
                        newdp[j] = True
                dp = newdp
            return any(dp)

        # バイナリサーチで最小の読み終わる時間を探す
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        read_end = left

        # 読む時間を決定して二人に割り振る (復元はしないが、読む時間の割り振りはdpで表せる)
        # dpで読む時間の割り当て例1つ見つける（dp復元）
        # 読み終わる時間=read_endで割り当て可能
        dp = [False]*(read_end+1)
        dp[0] = True
        prev = [-1]*(read_end+1)
        for r, _ in books:
            newdp = [False]*(read_end+1)
            newprev = [-1]*(read_end+1)
            for j in range(read_end+1):
                if not dp[j]:
                    continue
                # jにrを追加
                if j + r <= read_end and not newdp[j+r]:
                    newdp[j+r] = True
                    newprev[j+r] = j
                if not newdp[j]:
                    newdp[j] = True
                    newprev[j] = j
            dp = newdp
            prev = newprev

        # dpの中でTrueなjから復元 読む時間をjとすると、一人の読む時間はj, もう一人はtotal_r-j
        for j in range(read_end, -1, -1):
            if dp[j]:
                a_read = j
                break
        b_read = total_r - a_read

        # 読む配分を復元して、どの本がどちらか決める
        a_set = set()
        idx = read_end
        for i in range(N-1, -1, -1):
            r, _ = books[i]
            if idx - r >= 0 and dp[idx - r] and prev[idx] == idx - r:
                a_set.add(i)
                idx -= r
            else:
                # this book in b side
                idx = idx

        # 感想文は本を読み終わったら順次可能。2人の読み終わる時間がread_endなので
        # 感想文は並行して書けるが、本は重複しないので、本ごとに感想文は片方ずつ.
        # 感想文終了時間はmax(アミの読む時間＋感想文合計, マミの読む時間＋感想文合計)
        a_write = sum(books[i][1] for i in a_set)
        b_write = sum(books[i][1] for i in range(N) if i not in a_set)
        ans = max(a_read + a_write, b_read + b_write)
        print(ans)

if __name__ == '__main__':
    solve()