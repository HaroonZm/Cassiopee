N, A, B = [int(x) for x in input().split()]
res = 0
def s(n):
    total = 0
    k = n
    while k:
        total += k % 10
        k //= 10
    return total

i = 0
while True:
    digitsum = s(i) if i else 0
    if (digitsum >= A) and (digitsum <= B):
        res = res + i
    i += 1
    if i > N:
        break
print(res)