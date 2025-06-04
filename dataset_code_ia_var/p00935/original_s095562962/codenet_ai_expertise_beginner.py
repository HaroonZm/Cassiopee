n = int(input())
numbers = []
for _ in range((n // 19) + (1 if n % 19 != 0 else 0)):
    line = input().split()
    numbers.extend(line)

all_numbers = ''.join(numbers)
i = 0

while True:
    if str(i) not in all_numbers:
        print(i)
        break
    i += 1