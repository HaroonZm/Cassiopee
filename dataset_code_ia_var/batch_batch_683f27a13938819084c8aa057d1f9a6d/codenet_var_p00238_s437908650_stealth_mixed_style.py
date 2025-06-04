from sys import stdin

def checker():
    while True:
        A = int(stdin.readline())
        if not A:
            break
        def get():
            return list(map(int, stdin.readline().split()))
        x = 0
        B = int(stdin.readline())
        for i in range(B):
            y0, y1 = get()
            x = x + y1 - y0
        if A > x:
            print(A - x)
        else:
            print('OK')

checker()