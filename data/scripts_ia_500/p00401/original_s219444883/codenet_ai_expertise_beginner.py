n = int(input())
i = 1
count = 0
while True:
    if n < 2**i:
        count = 2**(i-1)
        break
    i = i + 1
print(count)