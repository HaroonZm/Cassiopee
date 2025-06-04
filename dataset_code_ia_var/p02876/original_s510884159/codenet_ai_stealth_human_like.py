import heapq
import sys
import random

# Une classe pour simuler un max-heap en inversant les signes, ça marche pas mal
class Heapq:
    def __init__(self, arr):
        self.que = []
        for a in arr:
            self.que.append(-a)  # on inverse pour faire max-heap, oups ici direct append...
        heapq.heapify(self.que) # va marcher quand même

    def pop(self):
        # Ici je remets le signe, pratique
        return -heapq.heappop(self.que)

    def push(self, a):
        heapq.heappush(self.que, -a)

    def top(self):
        return -self.que[0]  # top simplement par l'index

# pour le segtree, valeur neutre super grande
def segfunc(x, y):
    return min(x, y)
ide_ele = 10 ** 15  # ça devrait être assez grand

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        # arrondit à la puissance de 2 au dessus (merci bit_length!)
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * (2 * self.num)
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            # alors là, je fais avec <<
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        # boucle classique sur les intervals, pas trop mal
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

input = sys.stdin.readline

N = int(input())
beam = []
for i in range(N):
    beam.append(tuple(map(int, input().split()))) # ça va, c'est classique

def solve2():
    # On trie par le 2ème élément
    beam.sort(key=lambda x: x[1])

    # Pré-calcul des data
    data = [min(0, beam[i][0] - beam[i][1]) for i in range(N)]
    for i in range(N - 2, -1, -1):
        data[i] += data[i + 1]

    cummin = [beam[i][1] for i in range(N)]
    for i in range(N):
        if beam[i][0] - beam[i][1] > 0:
            cummin[i] = 10 ** 15

    for i in range(N - 2, -1, -1):
        cummin[i] = min(cummin[i], cummin[i + 1])

    # test pour un m donné
    def cond(m):
        if m == 0:
            if data[0] <= 0:
                return True
            else:
                return False

        que = Heapq([])
        cnt = 0
        S = 0
        for i in range(N - 1):
            if cnt == m:
                # On teste si on peut remplacer un max
                test = que.top()
                if beam[i][0] < test:
                    que.pop()
                    que.push(beam[i][0])
                    S += beam[i][0] - test
            else:
                que.push(beam[i][0])
                S += beam[i][0]
                cnt += 1
            if cnt == m:
                test = S + data[i + 1]
                if test <= 0:
                    return True
        return False

    start = 0
    end = N
    # Une binaire search histoire d'optimiser
    while end - start > 1:
        test = (end + start) // 2
        if cond(test):
            start = test
        else:
            end = test

    if not cond(0):
        print("0 1")
        exit()
    m = start
    ans = [0, 1]
    que = Heapq([])
    cnt = 0
    S = 0

    if m != 0:
        for i in range(N - 1):
            if cnt == m:
                # encore ce replace de max
                test = que.top()
                if beam[i][0] < test:
                    que.pop()
                    que.push(beam[i][0])
                    S += beam[i][0] - test
            else:
                que.push(beam[i][0])
                S += beam[i][0]
                cnt += 1
            if cnt == m:
                test = S + data[i + 1]
                B = cummin[i + 1]
                if test <= 0:
                    t = abs(test)
                    if B * ans[0] < ans[1] * t:
                        ans = [t, B]

        # initialisation
        startL = [-1] * N
        endL = [-1] * N
        que2 = []
        trash = []
        cnt2 = 0
        S2 = 0
        data1 = [ide_ele] * N
        data2 = [ide_ele] * N
        for i in range(N):
            if cnt2 == m:
                # On bosse sur les deux heaps et indices
                val, idd = que2[0]
                val = -val
                if val > beam[i][0]:
                    heapq.heappop(que2)
                    heapq.heappush(trash, val)
                    endL[idd] = i - 1
                    heapq.heappush(que2, (-beam[i][0], i))
                    startL[i] = i
                    S2 += beam[i][0] - val
                else:
                    heapq.heappush(trash, beam[i][0])
            else:
                heapq.heappush(que2, (-beam[i][0], i))
                startL[i] = i
                S2 += beam[i][0]
                cnt2 += 1
            if cnt2 == m:
                if i != N - 1:
                    data1[i] = S2 + data[i + 1]
                    if trash:
                        data2[i] = S2 + data[i + 1] + trash[0]
                    else:
                        data2[i] = S2 + data[i + 1]
                else:
                    data1[i] = S2
                    if trash:
                        data2[i] = S2 + trash[0]
                    else:
                        data2[i] = S2

        for i in range(N):
            if startL[i] != -1 and endL[i] == -1:
                endL[i] = N - 1

        Seg1 = SegTree(data1, segfunc, ide_ele)
        Seg2 = SegTree(data2, segfunc, ide_ele)

        for i in range(m):
            if endL[i] == m - 1:
                temp = Seg1.query(m, N)
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp:
                        ans = [temp, B]
            else:
                L, R = m, endL[i]
                temp = Seg2.query(L, R + 1) - beam[i][0]
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp:
                        ans = [temp, B]
                temp = Seg1.query(R + 1, N)
                temp += beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp:
                        ans = [temp, B]
        for i in range(m, N):
            if beam[i][0] - beam[i][1] <= 0:
                if startL[i] == -1:
                    temp = Seg1.query(i, N)
                    temp += beam[i][0] - beam[i][1]
                    if temp <= 0:
                        temp = abs(temp)
                        B = beam[i][1]
                        if B * ans[0] < ans[1] * temp:
                            ans = [temp, B]
                else:
                    L = startL[i]
                    R = endL[i]
                    temp = Seg2.query(L, R + 1) - beam[i][0]
                    temp += beam[i][0] - beam[i][1]
                    if temp <= 0:
                        temp = abs(temp)
                        B = beam[i][1]
                        if B * ans[0] < ans[1] * temp:
                            ans = [temp, B]
                    temp = Seg1.query(R + 1, N)
                    temp += beam[i][0] - beam[i][1]
                    if temp <= 0:
                        temp = abs(temp)
                        B = beam[i][1]
                        if B * ans[0] < ans[1] * temp:
                            ans = [temp, B]
            else:
                if startL[i] == -1:
                    temp = Seg1.query(m - 1, N)
                    temp += beam[i][0] - beam[i][1]
                    if temp <= 0:
                        temp = abs(temp)
                        B = beam[i][1]
                        if B * ans[0] < ans[1] * temp:
                            ans = [temp, B]
                else:
                    L = startL[i]
                    R = endL[i]
                    temp = Seg2.query(L, R + 1) - beam[i][0]
                    temp += beam[i][0] - beam[i][1]
                    if temp <= 0:
                        temp = abs(temp)
                        B = beam[i][1]
                        if B * ans[0] < ans[1] * temp:
                            ans = [temp, B]
                    temp = min(Seg1.query(R + 1, N), Seg1.query(m - 1, L))
                    temp += beam[i][0] - beam[i][1]
                    if temp <= 0:
                        temp = abs(temp)
                        B = beam[i][1]
                        if B * ans[0] < ans[1] * temp:
                            ans = [temp, B]

    else:
        for i in range(N):
            test = data[i]
            B = cummin[i]
            if test <= 0:
                t = abs(test)
                if B * ans[0] < ans[1] * t:
                    ans = [t, B]
        M = min(data)
        for i in range(N):
            if beam[i][0] - beam[i][1] > 0:
                temp = M + beam[i][0] - beam[i][1]
                if temp <= 0:
                    temp = abs(temp)
                    B = beam[i][1]
                    if B * ans[0] < ans[1] * temp:
                        ans = [temp, B]

    p, q = ans
    res = [q * m + p, N * q]
    from math import gcd
    g = gcd(res[0], res[1])
    return (res[0] // g, res[1] // g)

# Appel principal (bon, un print classique à la fin)
print(*solve2())