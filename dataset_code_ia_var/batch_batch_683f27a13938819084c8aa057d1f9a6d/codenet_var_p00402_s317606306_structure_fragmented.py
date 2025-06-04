def get_input():
    return int(input())

def get_house_positions():
    return list(map(int, input().split()))

def initialize_min():
    return 10000

def initialize_range():
    return 2001

def initialize_dis():
    return []

def calculate_distance_for_house(house_position, j):
    return abs(house_position - j)

def fill_dis_for_j(house, j):
    dis = initialize_dis()
    for i in range(len(house)):
        distance = calculate_distance_for_house(house[i], j)
        dis.append(distance)
    return dis

def get_max_distance(dis):
    return max(dis)

def update_min(current_min, candidate):
    if candidate < current_min:
        return candidate
    else:
        return current_min

def print_result(res):
    print(res)

def main():
    n = get_input()
    house = get_house_positions()
    curr_min = initialize_min()
    rng = initialize_range()
    for j in range(rng):
        dis = fill_dis_for_j(house, j)
        max_dis = get_max_distance(dis)
        curr_min = update_min(curr_min, max_dis)
    print_result(curr_min)

main()