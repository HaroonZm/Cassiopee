from collections import Counter
N = int(input())
S = input()

freq = Counter(S)
positions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
center = (1,1)

dist = [abs(r - center[0]) + abs(c - center[1]) for r,c in positions]

digits = [str(d) for d in range(1,10)]
freq_list = [(freq[d], d) for d in digits]
freq_list.sort(key=lambda x: (-x[0], x[1]))

pos_dist_digit = list(zip(dist, digits))
pos_dist_digit.sort(key=lambda x:(x[0], x[1]))

# Map digit to its freq rank order
digit_order = {d:i for i,(f,d) in enumerate(freq_list)}

# Assign digits to positions sorted by distance asc then digit asc
# We try to assign the most frequent digits to closest positions
assign = [None]*9
used = set()
assign_idx = 0

# Sort positions by distance asc, digit asc (initially digits sorted)
# We assign digits in freq order to positions by distance
digits_assigned = ['']*9
for i, (dist_pos, pos_digit) in enumerate(pos_dist_digit):
    digits_assigned[i] = pos_digit

# Map digit to position index in digits_assigned
pos_for_digit = {}

assigned_positions = [None]*9
# We'll assign positions in order of increasing dist
# For digits, assign in freq order, tie break by digit asc
digits_assign_order = [d for _,d in freq_list]

# Assign digits to positions in order of dist ascending, digit asc
positions_sorted = sorted(range(9), key=lambda i:(dist[i], digits_assigned[i]))
res = ['']*9

# We'll assign digit with highest freq to closest position
for p, d in zip(positions_sorted, digits_assign_order):
    res[p] = d

# Now fill remaining digits if any (digits with zero frequency), in digit asc order
assigned = set(res)
idx_free = 0
for d in digits:
    if d not in assigned:
        while res[idx_free] != '':
            idx_free += 1
        res[idx_free] = d
        assigned.add(d)

# Output in 3 lines of 3 chars
print(''.join(res[0:3]))
print(''.join(res[3:6]))
print(''.join(res[6:9]))