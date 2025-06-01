def fizzbuzz_check(x, s):
    if x % 15 == 0:
        return s == "FizzBuzz"
    if x % 3 == 0:
        return s == "Fizz"
    if x % 5 == 0:
        return s == "Buzz"
    return s == str(x)

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    sayings = [input().strip() for _ in range(n)]
    alive = [True]*m
    current_number = 1
    alive_count = m
    idx = 0
    player_idx = 0
    while idx < n and alive_count > 1:
        while not alive[player_idx]:
            player_idx = (player_idx + 1) % m
        if not fizzbuzz_check(current_number, sayings[idx]):
            alive[player_idx] = False
            alive_count -= 1
            current_number += 1
            player_idx = (player_idx + 1) % m
            idx += 1
            continue
        current_number += 1
        player_idx = (player_idx + 1) % m
        idx += 1
    # If only one player remains, ignore remaining sayings
    # If more remain, all sayings processed
    # Output alive players in ascending order
    print(*[i+1 for i, a in enumerate(alive) if a])