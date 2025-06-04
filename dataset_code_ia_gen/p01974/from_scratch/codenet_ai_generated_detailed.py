# 鳩ノ巣原理を利用した問題の解法
# 問題の要点：
# - N個の異なる自然数a_iが与えられる
# - 差がN-1の倍数であるペア(x, y)を1つ出力せよ
# - そのようなペアは必ず存在する

# 考え方：
# 差がN-1の倍数であるとは、(x - y) % (N-1) == 0 が成り立つこと。
# つまり、2つの数の値を (N-1) で割った余りが等しいペアを見つければよい。
# 鳩ノ巣原理により、N個の数を(N-1)個のクラスに分けると、
# 少なくとも1つのクラスに2つ以上の数が属し、その差は(N-1)の倍数になる。

def main():
    N = int(input())
    a = list(map(int, input().split()))
    
    # (N-1)で割った余りのクラス分けを辞書で保持
    remainder_groups = dict()
    
    for num in a:
        r = num % (N-1)
        if r in remainder_groups:
            # 余りが同じ既存の数がある → ペア成立
            print(num, remainder_groups[r])
            return
        else:
            remainder_groups[r] = num

if __name__ == "__main__":
    main()