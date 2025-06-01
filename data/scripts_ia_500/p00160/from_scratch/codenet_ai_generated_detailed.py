# 配送料金計算プログラム

# このプログラムは複数のデータセットに対して、
# 荷物の縦横高さの和（大きさ）と重さを基に宅配料金を計算し、
# 各データセットの料金の合計を出力するものです。
# サイズはAからFまであり、サイズごとに大きさ・重さの上限がある。
# Fサイズを超える荷物は料金対象外となる。

def calculate_fee(size_sum, weight):
    """
    大きさの合計と重さから料金を判定する関数。
    大きさリスト、重さリスト、料金リストは両方の条件を満たす最小の料金を判定。
    条件を満たすサイズがなければ0を返す（対象外）。
    """
    # サイズ別の大きさ上限(cm)
    size_limits = [60, 80, 100, 120, 140, 160]
    # サイズ別の重さ上限(kg)
    weight_limits = [2, 5, 10, 15, 20, 25]
    # サイズ別料金(円) A～F
    fees = [600, 800, 1000, 1200, 1400, 1600]

    # 可能なサイズの中で、最初に大きさと重さ両方を満たすところの料金を返す
    for i in range(len(size_limits)):
        if size_sum <= size_limits[i] and weight <= weight_limits[i]:
            return fees[i]
    # どのサイズにも当てはまらない場合は対象外
    return 0

def main():
    import sys

    # 1行ずつ入力を読み込みデータセットごとに処理
    while True:
        line = ''
        # 空行やスペースだけの行があればスキップ
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                # 入力終了（EOF）
                return
        n = int(line.strip())
        if n == 0:
            # 0で入力終了なので終了
            break

        total_fee = 0
        for _ in range(n):
            x, y, h, w = map(int, sys.stdin.readline().split())
            size_sum = x + y + h  # 大きさの三辺の和
            fee = calculate_fee(size_sum, w)
            total_fee += fee

        print(total_fee)

if __name__ == '__main__':
    main()