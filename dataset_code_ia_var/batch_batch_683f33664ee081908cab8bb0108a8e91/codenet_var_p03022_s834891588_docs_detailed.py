"""
このプログラムは高速ウォルシュ・ハダマード変換（FWHT）を利用して、特殊な畳み込み方程式を効率的に解きます。
与えられた数列 A から、ある数列 B（x0 = 0）を復元する流れです。
変換や逆変換、正規化、そして最終補正処理を行っており、各工程に詳細なコメントと docstring を添えています。
"""

MOD = 998244353  # 使用する法（素数）

def fwht(a):
    """
    高速ウォルシュ・ハダマード変換 (Fast Walsh–Hadamard Transform) を配列 a に作用させる

    Args:
        a (list of int): 変換したい長さ2^Nの整数リスト（破壊的に変換される）
    Returns:
        None
    """
    N = len(a)
    i = 1
    while i < N:
        j = 0
        while j < N:
            for k in range(i):
                x = a[j + k]
                y = a[i + j + k]
                # 和と差をMODで更新
                a[j + k] = (x + y) % MOD
                a[i + j + k] = (x - y) % MOD
            j += i << 1
        i <<= 1

def inv(x):
    """
    ある整数 x に対するMOD逆元（乗法逆数）を返す

    Args:
        x (int): 逆元を取る対象の整数
    Returns:
        int: x の MOD 逆元
    """
    return pow(x, MOD - 2, MOD)

def main():
    """
    メイン処理。入力の受け取り、正規化、高速変換、逆変換、補正、そして出力まで処理する。
    """

    # 入力の受け取り
    N = int(input())  # N: 2^N が数列長
    A = [int(i) for i in input().split()]  # 入力配列
    NN = 1 << N  # NN = 2^N

    # 1. A の正規化: ∑A[i]=1 となるようにスケーリング
    s = inv(sum(A) % MOD)  # ∑A[i] の逆元
    for i in range(NN):
        A[i] = (A[i] * s) % MOD
    # a0-1にしておく（解がx0=0となる性質利用の準備）  
    A[0] = (A[0] - 1) % MOD

    # 2. A を高速ウォルシュ・ハダマード変換
    fwht(A)

    # 3. Cの右辺（Bの目標和）のFWHTも準備する
    # B: [NN-1, -1, -1, ..., -1] の配列
    B = [-1] * NN
    B[0] = (NN - 1) % MOD
    fwht(B)

    # 4. AのFWHTで割ってBのFWHTを復元する（C[i] = B[i]/A[i])
    C = [(inv(A[i]) * B[i]) % MOD for i in range(NN)]

    # 5. 逆FWHT: 再びFWHTをかけて1/NN倍すればinverseになる
    fwht(C)
    inv_NN = inv(NN)
    for i in range(NN):
        C[i] = (C[i] * inv_NN) % MOD

    # 6. 解の補正（x0=0に対応）。各要素からC[0]（=x0）を引く
    for i in range(NN):
        print((C[i] - C[0]) % MOD)

# 直接実行された場合のみmain()を呼び出す
if __name__ == "__main__":
    main()