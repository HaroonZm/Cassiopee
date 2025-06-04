import math
from decimal import Decimal, ROUND_HALF_UP

def process_test_case():
    seq_primary = tuple(sorted(map(int, input().split()), reverse=True))
    seq_secondary = tuple(sorted(map(int, input().split())))
    win_count = 0
    state_sums = {(): (0, 0)}
    for idx_turn in range(9):
        next_state_sums = {}
        for used_indices in state_sums:
            for elem_secondary in seq_secondary:
                if elem_secondary not in used_indices:
                    sum_primary = state_sums[used_indices][0] + (seq_primary[idx_turn] + elem_secondary) * (seq_primary[idx_turn] > elem_secondary)
                    sum_secondary = state_sums[used_indices][1] + (seq_primary[idx_turn] + elem_secondary) * (seq_primary[idx_turn] < elem_secondary)
                    if sum_primary > 85:
                        win_count += math.factorial(8 - idx_turn)
                    elif sum_secondary < 86:
                        extended_indices = tuple(list(used_indices) + [elem_secondary])
                        next_state_sums[extended_indices] = (sum_primary, sum_secondary)
        state_sums = next_state_sums
    win_probability = win_count / 362880
    loss_probability = 1 - win_probability
    print(
        "{} {}".format(
            Decimal(win_probability).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP),
            Decimal(loss_probability).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
        )
    )

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        process_test_case()

main()