import sys
sys.setrecursionlimit(10**7)

class AhoCorasick:
    def __init__(self):
        self.next = [{}]
        self.fail = [-1]
        self.output = [False]

    def add_word(self, word):
        cur = 0
        for c in word:
            if c not in self.next[cur]:
                self.next[cur][c] = len(self.next)
                self.next.append({})
                self.fail.append(-1)
                self.output.append(False)
            cur = self.next[cur][c]
        self.output[cur] = True

    def build(self):
        from collections import deque
        q = deque()
        for c, nxt in self.next[0].items():
            self.fail[nxt] = 0
            q.append(nxt)
        while q:
            r = q.popleft()
            if self.output[self.fail[r]]:
                self.output[r] = True
            for c, nxt in self.next[r].items():
                self.fail[nxt] = self.next[self.fail[r]].get(c, 0)
                if self.output[self.fail[nxt]]:
                    self.output[nxt] = True
                q.append(nxt)

def main():
    input = sys.stdin.readline
    N = int(input())
    ac = AhoCorasick()
    for _ in range(N):
        s = input().strip()
        length = len(s)
        for i in range(length):
            for j in range(i+1,length+1):
                ac.add_word(s[i:j])
    ac.build()

    from collections import deque
    q = deque()
    q.append( (0, '') )
    while q:
        state, res = q.popleft()
        for c in map(chr, range(97,123)):
            nxt = ac.next[state].get(c,0)
            if not ac.output[nxt]:
                print(res + c)
                return
            else:
                # we can enqueue to explore longer strings if needed
                # but it is not necessary to enqueue here because
                # BFS guarantees shortest length and lex order.
                pass

if __name__ == "__main__":
    main()