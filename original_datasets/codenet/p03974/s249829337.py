# 文字列の問題で、同じような文字列をまとめたいので、
# どう考えても Trie を使いたい気持ちになる

# あとは適当にやったらなんとかなった
# 1100 点の割には簡単っぽい

class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0  # 自身を含めた部分木の大きさ

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        node = self.root
        node.count += 1
        for c in s:
            c = ord(c) - 97
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
            node.count += 1
        node.child[26] = TrieNode()
        node.child[26].count += 1

    def query(self, s):
        res = [[0]*27 for _ in range(26)]
        node = self.root
        for c in s:
            c = ord(c) - 97
            res_c = res[c]
            for i, child in node.child.items():
                res_c[i] += child.count
            node = node.child[c]
        return res

from itertools import groupby
import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    S = [input()[:-1] for _ in range(N)]
    trie = Trie()
    for s in S:
        trie.add(s)

    Q = int(input())
    KP = [input().split() for _ in range(Q)]
    Ans = [-1] * Q
    Idx_Q = sorted(range(Q), key=lambda x: KP[x][0])
    for v, g in groupby(Idx_Q, key=lambda x: KP[x][0]):
        K = int(v) - 1
        L_K = trie.query(S[K])
        for idx in g:
            _, P = KP[idx]
            P = [ord(c) - 97 for c in P]
            ans = 1
            for i, pi in enumerate(P):
                for pj in P[:i]:
                    ans += L_K[pi][pj]
                ans += L_K[pi][26]
            Ans[idx] = ans
    print("\n".join(map(str, Ans)))

main()