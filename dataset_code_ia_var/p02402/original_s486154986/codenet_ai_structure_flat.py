num = int(input())
numbers = []
for i in input().split():
    numbers.append(int(i))
min_num = numbers[0]
max_num = numbers[0]
sum_num = 0
for n in numbers:
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
    sum_num += n
print(min_num, max_num, sum_num)