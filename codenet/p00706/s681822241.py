def get_data():
    data = int(input())
    return data

def get_data_list():
    data_list = input().split()
    for i, v in enumerate(data_list):
        data_list[i] = int(v)
    return data_list

class MakePositionEasy:

    def __init__(self, data):
        self.w = data[0]
        self.h = data[1]

def get_all_persimmon_coordinate(persimmon_num):
    all_persimmon_coordinate = [None] * persimmon_num
    for i in range(persimmon_num):
        all_persimmon_coordinate[i] = tuple(get_data_list())
    all_persimmon_coordinate = set(all_persimmon_coordinate)
    return all_persimmon_coordinate

def make_persimmon_map(area_size, all_persimmon_coordinate):
    persimmon_map = [[0] * (area_size.w + 1) for i in range(area_size.h + 1)]
    for w in range(1, area_size.w+1):
        current_line_count = 0
        for h in range(1, area_size.h+1):
            if (w,h) in all_persimmon_coordinate:
                current_line_count += 1
            bef_num = persimmon_map[h][w-1]
            persimmon_map[h][w] = (bef_num + current_line_count)
    return persimmon_map

def get_max_num(persimmon_map,area_size, given_size):
    max_num = 0
    for w in range(given_size.w, area_size.w+1):
        for h in range(given_size.h, area_size.h+1):
            persimmon_num = calculate_persiommon_num(persimmon_map, given_size, w, h)
            if persimmon_num > max_num:
                max_num = persimmon_num
    return max_num

def calculate_persiommon_num(persimmon_map , given_size, w, h):
    persimmon_num = persimmon_map[h][w]
    persimmon_num -= persimmon_map[h-given_size.h][w]
    persimmon_num -= persimmon_map[h][w-given_size.w]
    persimmon_num += persimmon_map[h-given_size.h][w-given_size.w]
    return persimmon_num

if __name__ == "__main__":
    while True:
        persimmon_num = get_data()
        if persimmon_num == 0:
            break
        area_size = MakePositionEasy(get_data_list())
        all_persimmon_coordinate = get_all_persimmon_coordinate(persimmon_num)
        given_size = MakePositionEasy(get_data_list())
        persimmon_map = make_persimmon_map(area_size, all_persimmon_coordinate)
        max_num = get_max_num(persimmon_map,area_size, given_size)
        print(max_num)