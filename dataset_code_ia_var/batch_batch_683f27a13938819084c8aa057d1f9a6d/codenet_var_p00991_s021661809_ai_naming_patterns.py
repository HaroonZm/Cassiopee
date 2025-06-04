MODULUS = 10**8 + 7
MAX_N = 1001

def compute_combination(total, select):
    if 2 * select > total:
        return compute_combination(total, total - select)
    return FACTORIAL_LIST[total] * INVERSE_LIST[select] * INVERSE_LIST[total - select] % MODULUS

FACTORIAL_LIST = [1] * (MAX_N + 1)
INVERSE_LIST = [1] * (MAX_N + 1)

for idx in range(2, MAX_N + 1):
    FACTORIAL_LIST[idx] = FACTORIAL_LIST[idx - 1] * idx % MODULUS

INVERSE_LIST[MAX_N] = pow(FACTORIAL_LIST[MAX_N], MODULUS - 2, MODULUS)
for idx in range(MAX_N - 1, 1, -1):
    INVERSE_LIST[idx] = INVERSE_LIST[idx + 1] * (idx + 1) % MODULUS

ROW_COUNT, COL_COUNT, VAL_A1, VAL_A2, VAL_B1, VAL_B2 = map(int, input().split())

MIN_ROW_DELTA = min(abs(VAL_B1 - VAL_A1), ROW_COUNT - abs(VAL_B1 - VAL_A1))
MIN_COL_DELTA = min(abs(VAL_B2 - VAL_A2), COL_COUNT - abs(VAL_B2 - VAL_A2))

result_value = 1
if MIN_ROW_DELTA * 2 == ROW_COUNT:
    result_value *= 2
if MIN_COL_DELTA * 2 == COL_COUNT:
    result_value *= 2

result_value *= compute_combination(MIN_ROW_DELTA + MIN_COL_DELTA, MIN_ROW_DELTA)
result_value %= MODULUS
print(result_value)