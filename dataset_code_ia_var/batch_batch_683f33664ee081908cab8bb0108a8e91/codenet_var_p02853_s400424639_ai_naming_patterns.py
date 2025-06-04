value_first, value_second = [int(item) for item in input().split()]
total_prize = 0
prize_mapping = {1: 300000, 2: 200000, 3: 100000}

if 1 <= value_first <= 3:
    total_prize += prize_mapping[value_first]

if 1 <= value_second <= 3:
    total_prize += prize_mapping[value_second]

if total_prize == 600000:
    total_prize = 1000000

print(total_prize)