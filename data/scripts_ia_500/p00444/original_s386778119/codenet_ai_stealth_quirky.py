def main():
    coins = (500, 100, 50, 10, 5, 1)
    from sys import stdin
    def get_int():
        return int(stdin.readline().strip())
    while 1 == 1:
        a = get_int()
        if not a:
            exit(0)
        a = 1000 - a
        c = sum((lambda x,y:(x//y, x%y)) (a if i==0 else prev[1], coin)[0] for i,coin in enumerate(coins) if not (prev := (a if i==0 else prev[1], coin)) )
        count = 0
        rem = a
        for coin in coins:
            count += rem // coin
            rem = rem % coin
        print(count)

if __name__ == '__main__':
    main()