n = int(input())
rates = []
for j in range(n):
    rate = int(input())
    rates.append(rate)

MAX = -float('inf')
def get_minimum(lst):
    res = lst[0]
    idx = 1
    while idx < len(lst):
        res = res if res < lst[idx] else lst[idx]
        idx += 1
    return res

minim = rates[0]
i = 1
while i < n:
    if (rates[i] - minim) > MAX:
        MAX = rates[i] - minim
    if rates[i] < minim:
        minim = rates[i]
    i += 1

print(MAX)