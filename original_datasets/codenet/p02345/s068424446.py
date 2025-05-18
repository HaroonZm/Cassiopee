INITIAL = 2 ** 31 - 1

class SegTreeMin:

    def __init__(self, V):
        # 元配列Vをセグメント木で表現する
        self.sz = len(V)
        N = 1
        while N < self.sz:
            N *= 2
        # ノードを初期化
        self.N = N
        self.node = [INITIAL] * (2 * self.N - 1)
        # ノードの最下段に元配列の値を挿入する
        for i in range(self.sz):
            self.node[i + self.N - 1] = V[i]
        # すべての段に値を挿入する
        for i in range(self.N-2,0,-1):
            self.node[i] = min(self.node[2*i+1], self.node[2*i+2])

    def update(self, x, val):
        '''
        x番目の要素をvalに更新する
        '''
        # 最下段のノードにアクセスする
        x += (self.N - 1)
        self.node[x] = val

        # 最下段のノードを更新したら、親を更新していく
        while x > 0:
            x = (x - 1) // 2
            self.node[x] = min(self.node[2*x+1], self.node[2*x+2])

    def get_min(self, a, b, k=0, l=0, r=-1):
        '''
        区間[a, b)の最小値をこたえる => 要求区間
        k := 自分がいるノードのインデックス
        [l,r)はノードがカバーする区間 => 対象区間
        '''
        # 最初に呼び出されたときのノードがカバーする区間は[0,N)
        if r < 0:
            r = self.N
        
        # 要求区間と対象区間が交わらない => 2147483647を返す
        if r <= a or l >= b:
            return INITIAL
        
        # 完全にカバーする場合
        if l >= a and r <= b:
            return self.node[k]

        # 一部分カバーする場合は子も探索する
        # 左側の子をvl 右側の子を vrとしている
        vl = self.get_min(a, b, 2*k+1, l, (l+r)//2)
        vr = self.get_min(a, b, 2*k+2, (l+r)//2, r)
        return min(vl, vr)

def main():
    n, q = map(int, input().split())
    V = [INITIAL] * n
    seg = SegTreeMin(V)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com:
            y += 1
            print(seg.get_min(x,y))
        else:
            seg.update(x,y)

if __name__ == "__main__":
    main()