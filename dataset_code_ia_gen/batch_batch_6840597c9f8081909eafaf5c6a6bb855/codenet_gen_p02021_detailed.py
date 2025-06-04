# 問題のポイント：
# コウさんはN日間、毎日同じ件数の仕事をすることにしたい。
# 日ごとに仕事がA_i件追加される。
# 仕事が残っている限りいくらでもこなせるが、毎日こなす仕事数は一定。
# そのとき、毎日こなせる最大の仕事数を求める。
#
# アプローチ：
# ・毎日やる仕事件数をxとする。
# ・xが大きいほど、早く仕事は減るが、仕事が前倒しで不足するかもしれない。
# ・xが小さいほど、最終的に残る仕事が多いかもしれないが、毎日の一定件数としては小さい。
# ・よって、xを二分探索（1から仕事の総和の最大値まで）で探し、
#   毎日x件の仕事をこなせるかどうかを判定する。
#
# 判定基準：
# ・日々の仕事量とこれまでの仕事累積を考慮し
# ・各日、累積仕事量 >= xなら次の日にx件処理しても足りると判断。
# これをN日繰り返し、処理できるならxは可能。
#
# この方法で最大xを求める。

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 仕事の合計が最大の毎日の仕事件数の上限となる
    total_jobs = sum(A)
    
    # 二分探索の範囲を設定
    left = 1  # 最低1件はこなしたい
    right = total_jobs  # 最大は全ての日の仕事合計
    
    def can_do(x):
        # x件/日で仕事できるか判定
        # 溜まった仕事の総数を累積しつつ、毎日x件処理していく
        accumulated = 0
        for i in range(N):
            accumulated += A[i]  # 仕事がi日目に追加される
            if accumulated < x:  # 仕事が足りなければx件は無理
                return False
            accumulated -= x  # x件仕事をこなす
        return True  # 全日程でx件処理可能
    
    # 二分探索で最大xを探す
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if can_do(mid):
            ans = mid  # midは可能
            left = mid + 1  # もっと大きい値を試す
        else:
            right = mid - 1  # midは不可能なので小さい値を試す
    
    print(ans)

if __name__ == "__main__":
    main()