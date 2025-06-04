# 各問題の得点を10行分入力として受け取り、その合計を計算して出力するプログラム

def main():
    total_score = 0  # 合計得点を保存する変数を初期化
    for _ in range(10):  # 10回繰り返す
        score = int(input())  # 問題の得点を整数として入力
        total_score += score  # 得点を合計に加算

    print(total_score)  # 合計得点を出力

if __name__ == "__main__":
    main()