coins = [1, 5, 10, 50, 100, 500]

def main():
    wallet = input().split()
    total = 0
    idx = 0
    while idx < len(coins):
        total += coins[idx] * int(wallet[idx])
        idx += 1

    print(0 if total < 1000 else 1)

if __name__ == "__main__":
    main()