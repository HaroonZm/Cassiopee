import numpy as np

DEG = 16
MOD = 10 ** 9 + 7

even_coef = np.array(
    [0, 530289159, 384702529, 781298570, 90480784, 891754269, 348592099, 833888760, 898908474,
     505425073, 312827475, 794140068, 663894405, 565007911, 300594255, 98196225], dtype=np.int64)
odd_coef = np.array(
    [0, 231379733, 814507152, 631092340, 912089085, 58225824, 706460451, 264043077, 508834119,
     558179703, 136167972, 662064550, 384875310, 496818569, 537065939, 98196225], dtype=np.int64)

t = int(input())
buf = []
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        m = n // 2
        coef = even_coef
    else:
        m = (n - 1) // 2
        coef = odd_coef

    ms = np.ones(DEG, dtype=np.int64)
    for i in range(1, DEG):
        ms[i] = ms[i - 1] * m % MOD

    ans = (ms * coef % MOD).sum() % MOD
    buf.append(ans)

print('\n'.join(map(str, buf)))