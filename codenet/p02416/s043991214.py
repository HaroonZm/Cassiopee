number = input()

while number != "0" :
    sum_number = 0
    for i in range(len(number)):
        sum_number += int(number[i])
    print(sum_number)
    number = input()