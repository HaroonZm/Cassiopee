# 定義されている演算子と数字のリスト
ops = ["+", "*", "-", "&", "^", "|"]  # 利用可能な演算子
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # 利用可能な数字

def check(x):
    """
    与えられた文字列xが有効な数式であるかどうかをチェックし、評価して整数値を返す。
    不正な数式（連続した演算子や不適切なゼロの使用、不正な始まり方など）の場合はNoneを返す。

    Args:
        x (str): 評価する数式文字列

    Returns:
        int or None: 有効なら評価した整数値、無効ならNone
    """
    # 連続した2つ以上の演算子を禁止
    op_count = 0
    for c in x:
        if c in ops:
            op_count += 1
            if op_count >= 2:
                return None  # 連続演算子は禁止
        else:
            op_count = 0

    # 数式の先頭や開きカッコ直後の演算子は禁止
    for op in ops:
        if x.startswith(op):
            return None
        if ("(" + op) in x:
            return None

    # 先頭に正しくないゼロがないかチェック
    zero_ok = False  # 直前が数字のときのみゼロを許可
    for c in x:
        if not zero_ok and c == "0":
            return None  # 無効なゼロの使用
        if c in numbers:
            zero_ok = True
        else:
            zero_ok = False

    # 有効な式の場合は評価して整数値を返す。例外時はNoneとする。
    try:
        return int(eval(x))
    except:
        return None

def get_nexts(x):
    """
    1文字削除または1文字追加によって作れる全ての有効な次の状態（式とその値）のリストを生成する。

    Args:
        x (str): 現在の数式文字列

    Returns:
        list of tuple: [(int, str), ...] 可能な次の操作で得られる値と対応する式
    """
    result = []
    # 1文字削除操作
    for i in range(len(x)):
        y = x[:i] + x[i + 1:]
        val = check(y)
        if val is not None:
            result.append((val, y))
    # 1文字追加操作
    for i in range(len(x) + 1):
        add_list = numbers + ops
        for s in add_list:
            y = x[:i] + s + x[i:]
            val = check(y)
            if val is not None:
                result.append((val, y))
    return result

def get_nexts_val(x):
    """
    1文字削除または1文字追加によって作れる全ての有効な次の状態の値だけのリストを生成する。

    Args:
        x (str): 現在の数式文字列

    Returns:
        list of int: 可能な次の操作で得られる値のリスト
    """
    result = []
    # 1文字削除操作
    for i in range(len(x)):
        y = x[:i] + x[i + 1:]
        val = check(y)
        if val is not None:
            result.append(val)
    # 1文字追加操作
    for i in range(len(x) + 1):
        add_list = numbers + ops
        for s in add_list:
            y = x[:i] + s + x[i:]
            val = check(y)
            if val is not None:
                result.append(val)
    return result

# メインループ
while True:
    # ユーザーからターン数と始めの式をスペース区切りで入力
    n, x = input().split(" ")
    n = int(n)
    # 入力nが0なら終了
    if n == 0:
        quit()

    # 次に到達できる全ての有効な式とその値を取得
    nexts = get_nexts(x)

    # ターン数が奇数の場合は最大値を取る
    if n % 2 == 1:
        # 値の降順にソートして最大値を持つものを出力
        nexts.sort(key=lambda a: -a[0])
        print(nexts[0][0])
        continue

    # ターン数が偶数の場合は相手が取りうる最小値を考え、それを最大化する
    minvals = []
    for (val, y) in nexts:
        nextss = get_nexts_val(y)
        nextss.sort()
        minvals.append(nextss[0])
    print(max(minvals))