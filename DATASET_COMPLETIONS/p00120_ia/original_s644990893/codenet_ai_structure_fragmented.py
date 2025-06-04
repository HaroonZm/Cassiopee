import math

def read_input():
    try:
        inp = raw_input()
        return map(int, inp.split())
    except EOFError:
        return None

def get_l_and_r(nums):
    if not nums:
        return None, None
    l = nums[0]
    r = nums[1:]
    return l, r

def is_simple_case(l, r):
    return 2 * sum(r) <= l

def sort_r(r):
    r.sort()
    return r

def build_s(n, r):
    s = []
    for i in xrange(n // 2):
        s = [r[i]] + s[::-1] + [r[-i-1]]
    return s

def append_mid_if_needed(s, n, r):
    mid = r[n // 2]
    if abs(s[0] - mid) < abs(s[-1] - mid):
        s.append(mid)
    else:
        s = [mid] + s
    return s

def calculate_ans(s):
    ans = s[0] + s[-1]
    for i in xrange(len(s) - 1):
        ans += 2 * math.sqrt(s[i] * s[i+1])
    return ans

def process_case(l, r):
    n = len(r)
    if n == 0:
        return "OK"
    if is_simple_case(l, r):
        return "OK"
    if n > 1:
        r = sort_r(r)
        s = build_s(n, r)
        if n & 1:
            s = append_mid_if_needed(s, n, r)
    else:
        s = r
    ans = calculate_ans(s)
    if ans < 0.000000001 + l:
        return "OK"
    else:
        return "NA"

def main():
    while True:
        nums = read_input()
        if nums is None:
            break
        l, r = get_l_and_r(nums)
        if l is None:
            break
        result = process_case(l, r)
        print result

main()