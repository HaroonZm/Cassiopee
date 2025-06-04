import sys

def is_mikomiko_string(S):
    n = len(S)
    # S = A B A B A の形になるためには、Sの長さは奇数である必要がある
    if n % 2 == 0:
        return None  # 偶数なら不可能

    # Sの長さ = 2 * len(A) + len(B)
    # ここで、len(B)は奇数なので、1 <= len(B) < n
    # len(A) = (n - len(B)) // 2
    # len(B)は奇数かつ正の整数で、len(B) < n
    # なるべく |AB| = len(A) + len(B) が最小となる組み合わせを探す

    # len(B)は奇数なので、1,3,5,...で試す
    for b_len in range(1, n, 2):
        if (n - b_len) % 2 != 0:
            continue  # (n - b_len) は2の倍数でなければならない
        a_len = (n - b_len) // 2
        if a_len <= 0:
            continue

        # インデックスでA, Bの部分文字列を抽出
        A = S[0:a_len]
        B = S[a_len:a_len + b_len]
        # SがA B A B A の形になっているか検証する
        if S == A + B + A + B + A:
            return A, B

    return None

def main():
    # 高速な入力読み込み
    S = sys.stdin.readline().rstrip('\n')

    result = is_mikomiko_string(S)
    if result is None:
        print("mitomerarenaiWA")
    else:
        A, B = result
        print(f"Love {A}!")

if __name__ == "__main__":
    main()