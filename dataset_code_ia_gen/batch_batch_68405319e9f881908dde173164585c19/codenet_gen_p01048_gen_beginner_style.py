N = int(input())

def count_divisors(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    return count

num = 1
while True:
    if count_divisors(num) == N:
        print(num)
        break
    num += 1