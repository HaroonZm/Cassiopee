def main():
    mod, pow3, pow3i, p = 2**61-1, [1]*400001, [1]*200001, 1
    i3 = pow(3, mod-2, mod)
    for i in range(1, 400001):
        pow3[i] = p = p*3 % mod
    p = 1
    for i in range(1, 200001):
        pow3i[i] = p = p*i3 % mod

    class rolling_hash():
        def __init__(self, seq, char_list=None):
            seq_size = self.seq_size = len(seq)  # 文字列の長さ
            mod = self.mod = 2**61-1  # mod
            Hash = self.Hash = [0]*(seq_size+1)  # 先頭からi-1文字目までのハッシュ値
            for i in range(seq_size):
                Hash[i+1] = (Hash[i] + (seq[i]+1) * pow3[i]) % mod

        def calc_hash(self, l, r):  # l文字目からr-1文字目までのハッシュ値
            return ((self.Hash[r]-self.Hash[l])*pow3i[l] % self.mod)

    n = int(input())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    memo = []

    a1 = rolling_hash([a[i-1] ^ a[i] for i in range(n)] +
                      [a[i-1] ^ a[i] for i in range(n)])
    b_hash = rolling_hash([b[i-1] ^ b[i] for i in range(n)]).calc_hash(0, n)
    for i in range(n):
        if a1.calc_hash(i, i+n) == b_hash:
            memo.append(i)
    b0 = b[0]
    for i in memo:
        x = b0 ^ a[i]
        print(i, x)

main()