name = ['A', 'B', 'C', 'D', 'E']
shop = []
while True:
    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])
    if a == 0 and b == 0:
        break
    s = a + b
    shop.append(s)
    if len(shop) == 5:
        biggest = shop[0]
        index = 0
        i = 1
        while i < 5:
            if shop[i] > biggest:
                biggest = shop[i]
                index = i
            i = i + 1
        print(name[index], biggest)
        shop = []