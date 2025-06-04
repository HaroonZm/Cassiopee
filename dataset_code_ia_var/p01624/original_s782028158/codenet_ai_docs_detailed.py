# 定義された演算子と数字のリスト
ops = ["+", "*", "-", "&", "^", "|"]  # 使用可能な演算子
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # 使用可能な数字

def check(x):
    """
    文字列xが有効な数式か検証し、その評価結果を整数で返す。

    - 同一箇所で演算子が2つ並ぶのはNG
    - 演算子で始まる/直後にかっこで始まるのはNG
    - 数字が先頭に0で始まっているのはNG
    - 上記チェック通過時は、安全にevalし、整数として返す
    - それら以外/エラーならNoneを返す
    
    Parameters
    ----------
    x : str
        検証対象の式文字列

    Returns
    -------
    int or None
        評価できればその整数値、無効/エラーの場合はNone
    """
    # 1. 演算子が2連続していないかチェック
    op = 0  # 連続する演算子の数
    for c in x:
        if c in ops:
            op += 1
            if op >= 2:
                return None  # 演算子の重複
        else:
            op = 0

    # 2. 演算子で始まる/演算子が(直後はダメ
    for op_sign in ops:
        if x.startswith(op_sign):
            return None
        if ("(" + op_sign) in x:
            return None

    # 3. 不正な0（数字列探索, 最初の数字が0になっていないか）
    zero_ok = False  # 直前が有効な数字か判定
    for c in x:
        if not zero_ok and c == "0":
            return None  # 最初の数字が0
        if c in ops:
            zero_ok = False
        elif c in numbers:
            zero_ok = True
        else:  # 括弧等
            zero_ok = False

    # 4. evalで整数値にできるなら返す、失敗したらNone
    try:
        val = int(eval(x))
        return val
    except:
        return None

def get_nexts(x):
    """
    現在の式xに対して1手で到達可能な次の状態(式)をすべて列挙し、その評価結果と式を返す。

    1. xの任意の1文字を削除した式を生成し、checkで妥当ならリストに追加
    2. xの任意の位置に数字や演算子を1文字挿入した式を生成し、checkで妥当ならリストに追加

    Parameters
    ----------
    x : str
        操作対象の式文字列

    Returns
    -------
    list of tuple(int, str)
        評価値と次状態文字列のタプルのリスト
    """
    result = []

    # 文字削除操作（各iについてx[i]を消す）
    for i in range(len(x)):
        y = x[:i] + x[i + 1:]  # i番目の文字を削除した新しい式
        val = check(y)
        if val is not None:
            result.append((val, y))

    # 文字挿入操作（各iに数字または演算子を入れてみる）
    for i in range(len(x) + 1):
        add_list = numbers + ops
        for s in add_list:
            y = x[:i] + s + x[i:]  # i番目にsを挿入
            val = check(y)
            if val is not None:
                result.append((val, y))

    return result

while True:
    # 入力フォーマット: 「手数 n」と「式x」をスペース区切りで受け取る
    n, x = input().split(" ")
    n = int(n)
    if n == 0:
        # n=0で終了
        quit()

    # 1手で到達可能な次の候補状態を取得
    nexts = get_nexts(x)

    if n % 2 == 1:
        # 先手の場合: 評価値が最大となる手を選択（降順ソート、最高値取得）
        nexts.sort(key=lambda a: -a[0])
        print(nexts[0][0])
        continue

    # 後手の場合: 各手で次の相手の最善（最小値）を考え、最大化する
    minvals = []
    for (val, y) in nexts:
        nextss = get_nexts(y)  # 相手が返す最善手（最小値）を選ぶ
        nextss.sort(key=lambda a: a[0])
        minvals.append(nextss[0][0])
    print(max(minvals))  # 最適応答のうち最大値を出力