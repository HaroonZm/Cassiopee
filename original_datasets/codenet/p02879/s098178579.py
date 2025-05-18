def solve():
    a,b = map(int, input().split())
    if 1<=a<=9 and 1<=b<=9:
        return a*b
    else:
        return -1

if __name__ == '__main__':
    print(solve())