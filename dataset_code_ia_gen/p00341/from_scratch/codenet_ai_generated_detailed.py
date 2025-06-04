# 解法の考え方：
# 直方体（箱）は3種類の辺の長さ a, b, c によって構成される。
# それぞれの辺が4本ずつ必要なので、12本の棒は長さごとに4本ずつのセットが3組存在する必要がある。
# したがって、棒の長さの集合を確認し、長さごとの本数が4本ずつ3組緩く整っているかを判定する。
#
# 実装上は棒の長さをソート後、同じ長さの棒が4本ずつ3セットできるか確認する方法がわかりやすい。

def can_form_cuboid(sticks):
    # 棒を長さでソートする
    sticks.sort()
    
    # 12本の棒を4本ずつ同じ長さで分割できるか確認する
    # つまり、0-3番目、4-7番目、8-11番目までの4本ごとに同じ長さかどうかを調べる
    for i in range(0, 12, 4):
        # 4本のうちの最初と最後が異なれば不成立
        if sticks[i] != sticks[i+3]:
            return False
    
    # さらに3セットの長さが必ず3種類である必要はない。
    # 立方体の場合は3種類のうち1種類や2種類でも良い。
    # よってここまでクリアすれば「yes」
    return True

def main():
    sticks = list(map(int, input().split()))
    if len(sticks) != 12:
        print("no")  # 入力条件外の場合安全対応
        return
    
    if can_form_cuboid(sticks):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()