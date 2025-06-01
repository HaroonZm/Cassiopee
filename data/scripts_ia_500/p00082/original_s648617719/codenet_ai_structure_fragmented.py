def compare_values(v1, v2):
    if v1 < v2:
        return False
    if v1 > v2:
        return True
    return None

def comp(lst1, lst2):
    for v1, v2 in zip(lst1, lst2):
        res = compare_values(v1, v2)
        if res is not None:
            return res
    return False

def read_input():
    return list(map(int, input().split()))

def calculate_unfit_passengers(plst, horse):
    count = 0
    for j in range(8):
        count += max(0, plst[j] - horse[j])
    return count

def rotate_horse(horse):
    first = horse.pop(0)
    horse.append(first)

def should_update_min(num, min_num, min_horse, horse):
    if num == min_num and comp(min_horse, horse):
        return True
    if num < min_num:
        return True
    return False

def update_min_values(num, min_num, min_horse, horse):
    if num < min_num:
        min_num = num
        min_horse = horse[:]
    elif num == min_num and comp(min_horse, horse):
        min_horse = horse[:]
    return min_num, min_horse

def process_one_case(plst):
    horse = [4, 1, 4, 1, 2, 1, 2, 1]
    min_num = 100000
    min_horse = horse[:]

    for _ in range(8):
        num = calculate_unfit_passengers(plst, horse)
        if should_update_min(num, min_num, min_horse, horse):
            min_num, min_horse = update_min_values(num, min_num, min_horse, horse)
        rotate_horse(horse)

    return min_horse

def print_horse(horse):
    print(" ".join(map(str, horse)))

def main_loop():
    while True:
        try:
            plst = read_input()
            min_horse = process_one_case(plst)
            print_horse(min_horse)
        except EOFError:
            break

main_loop()