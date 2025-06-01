lst = list()
i = 0
while i < 5:
    a = int(input())
    a = a if a >= 40 else 40
    lst.append(a)
    i += 1

def average(numbers):
    total, count = 0, 0
    for num in numbers:
        total += num
        count += 1
    return total // count

print(average(lst))