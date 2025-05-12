coins = [1, 5, 10, 50, 100 ,500]

if __name__ == "__main__":
    wallet = list(map(int, input().split()))
    sum = 0
    for i in range(6):
        sum += (coins[i] * wallet[i])

    print(1 if sum >= 1000 else 0)