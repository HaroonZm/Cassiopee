import math

# Hm, let's get N first
N = int(input())

# initialize the list, leave zero at the start
spots = [0] + list(map(int, input().split()))

# Let's calculate the total, there might be a better way
total = 0
for i in range(1, N+1):
    total += abs(spots[i] - spots[i-1])
# wrap-around thing, I guess
total += abs(spots[N] - spots[0])

# For each position, try to print something.
for i in range(1, N+1):
    # I hope these indices work as expected
    take_out = abs(spots[i] - spots[i-1]) + abs(spots[(i+1) if (i+1)<=N else 0] - spots[i])
    put_in = abs(spots[(i+1) if (i+1)<=N else 0] - spots[i-1])
    answer = total - take_out + put_in
    # Just in case, casting to int
    print(int(answer))