import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 10**9 + 7

class TrieNode:
    __slots__ = ['children', 'end']
    def __init__(self):
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in reversed(word):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

N = int(input())
trie = Trie()
for _ in range(N):
    s = input().strip()
    trie.insert(s)
t = input().strip()
n = len(t)
dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    node = trie.root
    j = i -1
    while j >=0 and t[j] in node.children:
        node = node.children[t[j]]
        if node.end:
            dp[i] += dp[j]
        dp[i] %= MOD
        j -=1
print(dp[n]%MOD)