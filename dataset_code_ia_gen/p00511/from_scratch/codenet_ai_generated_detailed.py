# 電卓プログラム（加減乗除を入力順で計算、割り算は切り捨て）
# 入力は交互に数値と演算子（+,-,*,/）が並び、最後に=で終了
# 優先順位は考えず、入力通りに計算
# 計算結果を=で出力し改行をつける

def main():
    import sys

    # 最初の数値を読み込み
    line = sys.stdin.readline()
    if not line:
        return
    result = int(line.strip())

    while True:
        # 演算子を読み込む
        op_line = sys.stdin.readline()
        if not op_line:
            break
        op = op_line.strip()
        if op == '=':
            # =なら結果出力して終了
            print(result)
            break

        # 数値を読み込む
        num_line = sys.stdin.readline()
        if not num_line:
            break
        num = int(num_line.strip())

        # 入力順に計算を行う（優先順位無し）
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            # 割り算は切り捨て
            if result * num < 0 and result % num != 0:
                # Pythonの整数除算は負の数で切り捨てではなく切り下げのため注意
                result = result // num + 1
            else:
                result = result // num
        else:
            # 想定外の演算子は無視または終了
            break

if __name__ == '__main__':
    main()