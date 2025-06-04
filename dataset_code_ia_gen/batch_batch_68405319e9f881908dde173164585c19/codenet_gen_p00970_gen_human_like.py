r, s, p = map(int, input().split())
passengers = [tuple(map(int, input().split())) for _ in range(p)]

# Calculate minimal steps for each passenger to evacuate
# For each passenger at (i, j):
# Steps to aisle = 0 if passenger is in aisle seat (j == s or j == s+1)
# else steps to aisle = distance to the nearest aisle seat
# Steps backward = number of rows from passenger's row to exit row (r - i + 1)
# Total steps = steps to aisle + steps backward

# The aisle seats are s-th seat (left aisle) and (s+1)-th seat (right aisle), since seats number from 1 to 2s
total_steps = 0
for i_k, j_k in passengers:
    if j_k == s or j_k == s + 1:
        steps_to_aisle = 0
    else:
        steps_to_aisle = min(abs(j_k - s), abs(j_k - (s + 1)))
    steps_backward = r - i_k + 1
    steps = steps_to_aisle + steps_backward
    total_steps = max(total_steps, steps)

print(total_steps)