import sys

def get_input_func():
    return sys.stdin.readline

def read_n(input_func):
    return int(input_func())

def read_a(input_func):
    return list(map(int, input_func().split()))

def sum_list(a):
    return sum(a)

def get_asum_half(asum):
    return asum / 2.0

def calc_fore_and_pre_sums(a, asumhalf):
    foresum = 0
    presum = 0
    for ai in a:
        foresum += ai
        if foresum >= asumhalf:
            break
        presum = foresum
    return foresum, presum

def calc_latsum(asum, s):
    return asum - s

def calc_diff(x, y):
    return abs(x - y)

def min_of_two(a, b):
    return min(a, b)

def main():
    input_func = get_input_func()
    n = read_n(input_func)
    a = read_a(input_func)
    asum = sum_list(a)
    asumhalf = get_asum_half(asum)
    foresum, presum = calc_fore_and_pre_sums(a, asumhalf)
    latsum = calc_latsum(asum, foresum)
    difa = calc_diff(foresum, latsum)
    latsum_presum = calc_latsum(asum, presum)
    difb = calc_diff(presum, latsum_presum)
    result = min_of_two(difa, difb)
    print(result)

main()