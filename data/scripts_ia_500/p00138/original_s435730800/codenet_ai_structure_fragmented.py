def read_input_line():
    line = input()
    return line

def parse_line_to_floats(line):
    parts = line.split()
    a = float(parts[0])
    b = float(parts[1])
    return a, b

def append_to_tmp(tmp, point):
    tmp.append(point)

def should_sort_and_process(i):
    return (i + 1) % 8 == 0

def sort_points_by_y(points):
    points.sort(key=lambda x: x[1])

def pushAns(d, ans):
    for j in range(2):
        ans.append((d[0][0], d[0][1]))
        d.pop(0)

def extend_data_with_tmp(data, tmp):
    data.extend(tmp)

def clear_tmp(tmp):
    tmp.clear()

def sort_data(data):
    data.sort(key=lambda x: x[1])

def print_ans(ans):
    for i in range(8):
        x = int(ans[i][0])
        y = ans[i][1]
        print(x, y)

def main():
    data = []
    tmp = []
    ans = []
    for i in range(24):
        line = read_input_line()
        a, b = parse_line_to_floats(line)
        append_to_tmp(tmp, (a, b))
        if should_sort_and_process(i):
            sort_points_by_y(tmp)
            pushAns(tmp, ans)
            extend_data_with_tmp(data, tmp)
            clear_tmp(tmp)
    sort_data(data)
    pushAns(data, ans)
    print_ans(ans)

main()