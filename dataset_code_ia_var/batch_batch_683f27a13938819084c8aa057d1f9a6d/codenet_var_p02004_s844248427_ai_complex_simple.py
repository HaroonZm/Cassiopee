from functools import reduce
from itertools import accumulate, cycle, groupby, islice
from operator import add

S = input()
direction_sequence = (
    1 if c == 'R' else -1 for c in S
)

# Accumulate directions to get current direction at each step
directions = list(accumulate(direction_sequence))

# Modulo trick: wrap at 4 and -4, so we keep running track where 4 or -4 triggers something
# Make a function to identify when a cumulative value reaches 4
def detect_four(seq):
    dq = 0
    for x in seq:
        dq = x
        yield dq

turns = list(detect_four(directions))

# Create indices where turn becomes 4, then count resets
fours = [i for i, v in enumerate(turns) if v == 4]

# Elaborate way to reset direction after 4/-4
def reset_acc(seq):
    direction = 0
    total = 0
    for c in seq:
        direction += c
        if direction == 4 or direction == -4:
            if direction == 4:
                total += 1
            direction = 0
        yield total

# We want the final count
result = list(reset_acc(1 if c == 'R' else -1 for c in S))
print(result[-1] if result else 0)