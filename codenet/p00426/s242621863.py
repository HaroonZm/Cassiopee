from collections import deque

def main():
    while True:
        n, m = [int(i) for i in input().split()]
        if n == 0 and m == 0:
            return
        _, *a = [int(i) for i in input().split()]
        _, *b = [int(i) for i in input().split()]
        _, *c = [int(i) for i in input().split()]
        a.insert(0, 0)
        b.insert(0, 0)
        c.insert(0, 0)

        q = deque()
        q.appendleft([a, b, c, 0, -1])
        tmp = [i for i in range(0, n+1)]

        while q:
            # d はカウンタ
            a, b, c, d, t = q.pop()
            """
            print(a)
            print(b)
            print(c)
            print('=======')
            """
            # 終了
            if d > m:
                print(-1)
                break
            if a == tmp or c == tmp:
                print(d)
                break
            # a から b
            if a[-1] > b[-1] and t != 1 and t != 0:
                q.appendleft([a[:-1], b+[a[-1]], c[:], d+1, 0])
            # b から a
            if b[-1] > a[-1] and t != 0 and t != 1:
                q.appendleft([a+[b[-1]], b[:-1], c[:], d+1, 1])
            # b から c
            if b[-1] > c[-1] and t != 3 and t != 2:
                q.appendleft([a[:], b[:-1], c+[b[-1]], d+1, 2])
            # c から b
            if c[-1] > b[-1] and t != 2 and t != 3:
                q.appendleft([a[:], b+[c[-1]], c[:-1], d+1, 3])

if __name__ == '__main__':
    main()