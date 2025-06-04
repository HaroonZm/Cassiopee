import sys

def wi():
    return list(map(int, sys.stdin.readline().split()))

def wip():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def ws():
    return sys.stdin.readline().split()

def si():
    return int(sys.stdin.readline())

def ss():
    return input()

def hi(n):
    result = []
    for _ in range(n):
        result.append(si())
    return result

def hs(n):
    result = []
    for _ in range(n):
        result.append(ss())
    return result

def s_list():
    return list(input())

def mi(n):
    result = []
    for _ in range(n):
        result.append(wi())
    return result

def mip(n):
    result = []
    for _ in range(n):
        result.append(wip())
    return result

def ms(n):
    result = []
    for _ in range(n):
        result.append(ws())
    return result

def num_grid(n):
    result = []
    for _ in range(n):
        row = sys.stdin.readline().split()[0]
        row_nums = [int(i) for i in row]
        result.append(row_nums)
    return result

def grid(n):
    result = []
    for _ in range(n):
        result.append(s_list())
    return result

def make_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

def main():
    a, b, k = map(int, input().split())
    a_list = make_divisors(a)
    b_list = make_divisors(b)

    common = []
    for i in a_list:
        if i in b_list:
            common.append(i)
    common = common[::-1]
    print(common[k - 1])

if __name__ == '__main__':
    main()