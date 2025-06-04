from functools import reduce

def read_int(): return int(input())
def collect_values(n):
    return list(map(lambda _: int(input()), range(n)))

def gen_table(sz):
    return [False for _ in range(sz+1)]

n = read_int()
seq = collect_values(n)
possible = gen_table(200*200)
possible[0] = True
max_sum = 0

for elem in seq:
    max_sum = max_sum + elem
    index = max_sum
    while index >= 0:
        if possible[index]:
            possible[index+elem] = True
        index = index - 1

for x in reversed(range(max_sum+1)):
    if x%10:
        if possible[x]:
            print(x)
            break
else:
    print(0)