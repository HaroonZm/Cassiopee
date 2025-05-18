import string

class SuffixArray:
    def __init__(self, S):
        self.N = len(S)
        self.S = S
        self.atoi = {x: i for i, x in enumerate(string.printable)}
        self.sa = self.__make_sa()

    def show(self):
        for i, s in enumerate(self.sa):
            print(i, s, self.S[s:])

    def __make_sa(self):
        """配列（文字列）Sのsuffix arrayを返す O(N(logN)^2)"""
        N = self.N
        SA = list(range(N + 1))
        rank = [-1] * (N + 1)
        tmp = [0] * (N + 1)
        k = 1

        for i, s in enumerate(self.S):
            rank[i] = self.atoi[s]

        def key(i):
            if i + k <= N:
                return (rank[i], rank[i + k])
            return (rank[i], -1)

        def cmp(i, j):
            return key(i) < key(j)

        while k <= N:
            SA.sort(key=key)
            tmp[SA[0]] = 0
            for i in range(1, N + 1):
                tmp[SA[i]] = tmp[SA[i - 1]] + cmp(SA[i - 1], SA[i])
            for i in range(N + 1):
                rank[i] = tmp[i]
            k *= 2
        return SA

    def contain(self, T, side="left"):
        """文字列SにTが含まれているかを返すO(|T|log|S|)
        input
            T: 検索する文字列（配列）
            side: left　-> S[sa[i]:sa[i]+NT] == Tとなる最小のindex iを返す
                  right -> 最大のindexを返す
        output:
            含まれる場合: S[sa[i]: sa[i]+NT] == Tとなる最小or最大のi
            含まれない場合: -1
        """
        NT = len(T)
        if NT > self.N:
            return -1
        L = 0
        R = self.N
        if side == "left":
            while R - L > 1:
                m = (L + R) // 2
                i = self.sa[m]
                if self.S[i:i + NT] < T:
                    L = m
                else:
                    R = m
            i = self.sa[R]
            if self.S[i:i + NT] == T:
                return R
        else:
            R += 1
            while R - L > 1:
                m = (L + R) // 2
                i = self.sa[m]
                if self.S[i:i + NT] <= T:
                    L = m
                else:
                    R = m
            i = self.sa[L]
            if self.S[i:i + NT] == T:
                return L
        return -1

    def get_indices(self, T):
        """Sの中に含まれるTの位置を格納したindexのリストを返す"""
        L = self.contain(T, side="left")
        if L == -1:
            return []
        R = self.contain(T, side="right")
        return [self.sa[i] for i in range(L, R+1)]

SA = SuffixArray(input())
res = SA.get_indices(input())
if res:
    res.sort()
    print(*res, sep="\n")