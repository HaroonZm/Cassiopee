N = int(input())
a = list(map(int, input().split()))
count = 0
for n in a:
    while True:
        if n % 2 == 0:
            count += 1
            n //= 2
        else:
            break
print(count)