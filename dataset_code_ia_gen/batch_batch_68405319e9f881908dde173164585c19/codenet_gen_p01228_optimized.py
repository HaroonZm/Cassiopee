import sys
input=sys.stdin.readline

# パターンを和音ごとに分割
def split_pattern(p):
    return [p[i:i+2] for i in range(0, len(p), 2)]

# 16進2桁文字列→整数変換（0-255）
def hex2int(h):
    return int(h,16)

# 整数→2桁大文字16進数文字列
def int2hex(i):
    return format(i,'02X')

for _ in range(int(input())):
    N = int(input())
    patterns = [input().rstrip('\n') for _ in range(N)]
    # 各パターンの分割
    parts = [split_pattern(p) for p in patterns]
    lengths = [len(p) for p in parts]
    max_len = max(lengths)
    # スケールアップするパターンの補間計算
    # 最大の分割数に合わせて他を拡大
    new_parts = []
    # 最大分割数は2048和音まで（4096文字）
    if max_len > 2048:
        print("Too complex.")
        continue

    for i, p in enumerate(parts):
        l = lengths[i]
        scale = max_len // l
        # max_lenはlの倍数なので割り切れる
        if scale == 1:
            new_parts.append(p)
        else:
            tmp = []
            for c in p:
                tmp.extend([c]*scale)
            new_parts.append(tmp)

    # 合成
    result = []
    for i in range(max_len):
        s = 0
        for p in new_parts:
            s |= hex2int(p[i])
        result.append(int2hex(s))
    # 表現長チェック
    # 文字数でなく和音数 * 2
    if len(result)*2 >2048:
        print("Too complex.")
        continue
    # 最短化 - 末尾から0の連続を削除しない（問題文で特に指定なし）
    # 特に問題文で最短化の詳細指定はないためそのまま出力
    print("".join(result))