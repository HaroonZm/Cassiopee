import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline
f_inf = float('inf')
mod = 1000000007

def main():
    x_y = input().split()
    x = int(x_y[0])
    y = int(x_y[1])
    if x % y == 0:
        print(-1)
    else:
        print(x)

if __name__ == '__main__':
    main()