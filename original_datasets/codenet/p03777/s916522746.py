def solve():
    a, b = input().split()
    if a == 'H':
        print(b)
    else:
        if b == 'H':
            print('D')
        else:
            print('H')

if __name__ == "__main__":
    solve()