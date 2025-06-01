def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_time(sec):
    h = sec // 3600
    sec %= 3600
    m = sec // 60
    s = sec % 60
    return h, m, s

for _ in range(3):
    data = list(map(int, input().split()))
    start_h, start_m, start_s = data[0], data[1], data[2]
    end_h, end_m, end_s = data[3], data[4], data[5]

    start_sec = time_to_seconds(start_h, start_m, start_s)
    end_sec = time_to_seconds(end_h, end_m, end_s)

    diff = end_sec - start_sec

    h, m, s = seconds_to_time(diff)
    print(h, m, s)