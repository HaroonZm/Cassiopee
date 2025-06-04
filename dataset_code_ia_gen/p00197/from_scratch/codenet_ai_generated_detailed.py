# ユークリッドの互除法を用いて最大公約数とステップ数を計算するプログラム

def gcd_with_steps(a, b):
    """
    ユークリッドの互除法でaとbの最大公約数を求める関数。
    同時に計算にかかったステップ数もカウントする。
    ステップの定義は「余りを求めてXに代入し、XとYを交換する操作1回」を1ステップとする。
    
    Parameters:
        a (int): 1つ目の整数
        b (int): 2つ目の整数
    
    Returns:
        (int, int): (最大公約数, ステップ数)
    """
    steps = 0
    x, y = a, b
    while y != 0:
        remainder = x % y  # 余りを計算
        x, y = y, remainder # Xに余りを代入しX,Yを入れ替え
        steps += 1
    # yが0になった時点のxが最大公約数
    return x, steps

def main():
    """
    標準入力から複数のデータセットを読み込み、それぞれに対して最大公約数とステップ数を計算し
    結果を出力する。
    入力の終わりは "0 0" で示される。
    """
    import sys
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a_str, b_str = line.split()
        a, b = int(a_str), int(b_str)
        # 入力の終端条件
        if a == 0 and b == 0:
            break
        
        gcd_val, step_count = gcd_with_steps(a, b)
        print(f"{gcd_val} {step_count}")

if __name__ == "__main__":
    main()