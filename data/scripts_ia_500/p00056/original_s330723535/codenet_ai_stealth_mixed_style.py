p = list(True for i in range(50000))
p[0] = 0

i = 2
while i < int(50000 ** 0.5) + 1:
    if p[i-1]:
        for j in range(i*i, 50000, i):
            p[j-1] = False
    i += 1

prime = []
for i in range(50000):
    if p[i]:
        prime.append(i+1)

def count_goldbach_partitions(n):
    count = 0
    half = n // 2
    for x in prime:
        if x > half:
            break
        if p[n - x - 1]:
            count += 1
    return count

while True:
    try:
        n = int(input())
        if n == 0:
            break
        print(count_goldbach_partitions(n))
    except Exception as e:
        break