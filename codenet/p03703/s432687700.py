import itertools
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        """
        :param int size:
        """
        self._bit = [0 for _ in range(size)]
        self._size = size

    def add(self, i, w):
        """
        i 番目に w を加える
        :param int i:
        :param int w:
        :return:
        """
        x = i + 1
        while x <= self._size:
            self._bit[x - 1] += w
            x += x & -x

    def sum(self, i):
        """
        0 番目から i 番目までの合計
        :param int i:
        :return:
        """
        ret = 0
        x = i + 1
        while x > 0:
            ret += self._bit[x - 1]
            x -= x & -x
        return ret

    def __len__(self):
        return self._size

N, K = list(map(int, sys.stdin.readline().split()))
A = [int(sys.stdin.readline()) for _ in range(N)]

# cumsum の最初を 0 にする
N += 1
# D[l-1] <= D[r] (l <= r) なら平均が K 以上。
D = list(itertools.accumulate([0] + [a - K for a in A]))

def compress(arr):
    """
    :param list of int arr:
    :return:
    """
    ret = [0] * len(arr)
    rank = 0
    prev = None
    for a, i in sorted([(a, i) for i, a in enumerate(arr)]):
        if a != prev:
            rank += 1
        ret[i] = rank
    return ret

def count(arr):
    """
    転倒数の逆。arr[L-1] <= arr[r] となる (L, r) の組み合わせ数
    :param list of int arr:
    :return:
    """
    ranks = compress(arr)
    bit = BinaryIndexedTree(size=max(ranks) + 1)
    ret = 0
    for i, rank in enumerate(ranks):
        ret += bit.sum(rank)
        bit.add(rank, 1)
    return ret

print(count(D))