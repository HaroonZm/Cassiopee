price = [1, 5, 10, 50, 100, 500]

def calculate_coins(total, available):
    coins_used = 0
    for i in range(len(price)-1, -1, -1):
        use = min(available[i], total // price[i])
        total -= use * price[i]
        coins_used += use
    return total, coins_used

while True:
    inputs = input().split()
    if inputs[0] == '0':
        break
    p = int(inputs[0])
    n = list(map(int, inputs[1:]))

    initial_sum = sum([a*b for a,b in zip(price, n)])

    answer = float('inf')

    for extra in range(1000):
        target = p + extra
        remaining, used_coins = calculate_coins(target, n)
        if remaining > 0:
            continue

        change_left = extra
        # utilisation d'une boucle while ici au lieu d'un for
        i = 5
        while i >= 0:
            used_coins += change_left // price[i]
            change_left %= price[i]
            i -= 1

        if used_coins < answer:
            answer = used_coins

    print(answer)