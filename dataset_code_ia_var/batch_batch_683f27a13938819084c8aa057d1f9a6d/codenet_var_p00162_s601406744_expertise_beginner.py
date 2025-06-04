import sys

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001

sys.setrecursionlimit(100000)

SIZE_2 = 20
SIZE_3 = 13
SIZE_5 = 9
NUM = 1000001

# Precompute powers of 2
POW_2 = [1] * SIZE_2
for i in range(1, SIZE_2):
    POW_2[i] = POW_2[i - 1] * 2

# Precompute powers of 3
POW_3 = [1] * SIZE_3
for i in range(1, SIZE_3):
    POW_3[i] = POW_3[i - 1] * 3

# Precompute powers of 5
POW_5 = [1] * SIZE_5
for i in range(1, SIZE_5):
    POW_5[i] = POW_5[i - 1] * 5

# Initialize the table
table = [0] * NUM

# Fill the table with valid numbers
for i in range(SIZE_2):
    for j in range(SIZE_3):
        if POW_2[i] * POW_3[j] >= NUM:
            break
        for k in range(SIZE_5):
            val = POW_2[i] * POW_3[j] * POW_5[k]
            if val >= NUM:
                break
            table[val] = 1

# Build prefix sums
for i in range(1, NUM):
    table[i] += table[i - 1]

# Answer the queries
while True:
    line = input()
    if line == "0":
        break
    left, right = map(int, line.split())
    print(table[right] - table[left - 1])