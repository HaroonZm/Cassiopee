#!/usr/bin/env python3

from collections import deque

class PriorityQueue:
    def __init__(self, size):
        self.tree = [None] * size
        self.bottom = 0

    def add(self, data):
        n = self.bottom
        self.bottom += 1
        self.tree[n] = data
        while n != 0:
            parent = (n - 1) // 2
            if self.tree[parent][1] < self.tree[n][1]:
                self.tree[parent], self.tree[n] = (
                    self.tree[n],
                    self.tree[parent],
                )
                n = parent
            else:
                return

    def top(self):
        return self.tree[0]

    def size(self):
        return self.bottom

    def pop_top(self):
        rv = self.tree[0]
        self.tree[0] = self.tree[self.bottom - 1]
        self.bottom -= 1
        n = 0
        while True:
            child1 = 2 * n + 1
            if child1 >= self.bottom:
                return rv
            child2 = 2 * n + 2
            if child2 >= self.bottom:
                child2 = child1

            if (
                self.tree[n][1] > self.tree[child1][1]
                and self.tree[n][1] > self.tree[child2][1]
            ):
                return rv
            elif self.tree[child1][1] > self.tree[child2][1]:
                self.tree[n], self.tree[child1] = (
                    self.tree[child1],
                    self.tree[n],
                )
                n = child1
            else:
                self.tree[n], self.tree[child2] = (
                    self.tree[child2],
                    self.tree[n],
                )
                n = child2
        return rv

def solve(N, M, A, B):
    ans = 0
    # 日付順にソートする
    all_works = deque(sorted(zip(A, B), key=lambda x: x[0]))
    pq = PriorityQueue(N)

    for d in range(1, M+1):
        # print('d=', d)
        # 今日が期限の仕事があれば追加
        while all_works and all_works[0][0] == d:
            work = all_works.popleft()
            pq.add(work)
        # print('all_works', all_works)
        # print('pq=', pq.tree)
        # 優先キューから最優先の仕事を選択する
        if pq.size():
            work = pq.pop_top()
            ans += work[1]

    return ans

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for idx in range(N):
        A[idx], B[idx] = map(int, input().split())

    ans = solve(N, M, A, B)

    print(ans)