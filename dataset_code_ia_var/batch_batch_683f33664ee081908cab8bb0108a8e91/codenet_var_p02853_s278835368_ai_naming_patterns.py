input_first_rank, input_second_rank = map(int, input().split())

prize_total = 0

rank_to_prize = {1: 300000, 2: 200000, 3: 100000}

if input_first_rank in rank_to_prize:
    prize_total += rank_to_prize[input_first_rank]
if input_second_rank in rank_to_prize:
    prize_total += rank_to_prize[input_second_rank]

if input_first_rank == 1 and input_second_rank == 1:
    prize_total += 400000

print(prize_total)