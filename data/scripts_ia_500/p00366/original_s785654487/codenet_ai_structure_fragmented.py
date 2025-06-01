def read_number():
    return int(input())

def read_timings(n):
    timings = []
    for _ in range(n):
        timings.append(read_number())
    return timings

def find_maximum(timings):
    max_value = 0
    for t in timings:
        if t > max_value:
            max_value = t
    return max_value

def find_divisors(max_t):
    divisors = []
    limit = (max_t >> 1) + 1
    for i in range(1, limit):
        if max_t % i == 0:
            divisors.append(i)
    divisors.append(max_t)
    return divisors

def calculate_adjustment(timings, divisors):
    adjustment = 0
    for t in timings:
        adjustment += find_closest_divisor_difference(t, divisors)
    return adjustment

def find_closest_divisor_difference(t, divisors):
    for d in divisors:
        if d >= t:
            return d - t
    return 0

def main():
    n = read_number()
    timings = read_timings(n)
    max_t = find_maximum(timings)
    divisors = find_divisors(max_t)
    adj = calculate_adjustment(timings, divisors)
    print(adj)

main()