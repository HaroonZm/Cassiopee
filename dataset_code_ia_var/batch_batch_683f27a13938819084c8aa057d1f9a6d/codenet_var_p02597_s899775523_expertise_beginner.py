N = int(input())
c = input()

r_count = c.count('R')

if r_count == 0 or r_count == len(c):
    print(0)
    exit()

swaps = 0

for i in range(r_count):
    if c[i] == 'W':
        swaps = swaps + 1

print(swaps)