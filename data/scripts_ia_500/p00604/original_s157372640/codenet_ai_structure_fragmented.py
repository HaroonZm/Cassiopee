def read_integer():
    try:
        return int(input())
    except:
        return None

def read_times():
    return list(map(int, input().split()))

def sort_times(times):
    times.sort()
    return times

def calculate_answer(num, times):
    result = 0
    for index, time in enumerate(times):
        result += (num - index) * time
    return result

def main_loop():
    while True:
        num = read_integer()
        if num is None:
            break
        times = read_times()
        times = sort_times(times)
        ans = calculate_answer(num, times)
        print(ans)

main_loop()