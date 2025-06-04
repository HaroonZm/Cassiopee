def bubble_sort(n, key=0):
    count = 0
    numbers = []
    for x in n:
        if isinstance(x, list):
            numbers.append(x)
        else:
            numbers.append([x])
    length = len(numbers) - 1
    for i in range(length):
        for j in range(length, i, -1):
            if numbers[j][key] < numbers[j-1][key]:
                tmp = numbers[j]
                numbers[j] = numbers[j-1]
                numbers[j-1] = tmp
                count += 1
    result = []
    for x in numbers:
        if len(x) == 1:
            result.append(x[0])
        else:
            result.append(x)
    return {'list': result, 'count': count}

def selection_sort(n, key=0):
    count = 0
    numbers = []
    for x in n:
        if isinstance(x, list):
            numbers.append(x)
        else:
            numbers.append([x])
    length = len(numbers)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if numbers[j][key] < numbers[min_index][key]:
                min_index = j
        if min_index != i:
            tmp = numbers[i]
            numbers[i] = numbers[min_index]
            numbers[min_index] = tmp
            count += 1
    result = []
    for x in numbers:
        if len(x) == 1:
            result.append(x[0])
        else:
            result.append(x)
    return {'list': result, 'count': count}

def card_format(cards):
    s = []
    for x in cards:
        s.append(str(x[0]) + str(x[1]))
    return " ".join(s)

if __name__ == '__main__':
    n = int(input())
    tmp = input().split(" ")
    c = []
    for item in tmp:
        c.append([item[0], int(item[1])])
    bubble_sorted = bubble_sort(c, 1)
    selection_sorted = selection_sort(c, 1)
    bubble_cards = card_format(bubble_sorted['list'])
    selection_cards = card_format(selection_sorted['list'])
    print(bubble_cards)
    print("Stable")
    print(selection_cards)
    if bubble_cards == selection_cards:
        print("Stable")
    else:
        print("Not stable")