# 解説：
# 直方体を作るためには、12本の棒が3組の辺の長さに分かれ、
# 各辺は4本ずつ（4辺ずつ同じ長さ）必要です。
# つまり、棒の長さが3種類あり、それぞれの長さがちょうど4本ずつでなければならない。
# 立方体も直方体の一種なので、1種類の長さが12本でも「yes」になる。

def can_form_cuboid(sticks):
    # 棒の本数は12本である前提
    if len(sticks) != 12:
        return False

    # 棒の長さの出現回数を数える
    from collections import Counter
    counter = Counter(sticks)

    # 直方体の辺の数は3種類で、それぞれ4本ずつ必要なので、
    # カウントの種類数は3か1（立方体の場合）でなければならない
    lengths = list(counter.values())
    # すべてのカウントが4かどうか確認
    if len(lengths) == 3 and all(count == 4 for count in lengths):
        return True
    # 立方体の場合は1種類の長さが12本
    if len(lengths) == 1 and lengths[0] == 12:
        return True

    return False

def main():
    # 入力を受け取る（1行12個の整数）
    sticks = list(map(int, input().split()))
    if can_form_cuboid(sticks):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()