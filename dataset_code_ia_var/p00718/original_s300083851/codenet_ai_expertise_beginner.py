import sys

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_str_list():
    return sys.stdin.readline().split()

def read_int():
    return int(sys.stdin.readline())

def main():
    results = []
    n = read_int()
    pairs = []
    for _ in range(n):
        items = read_str_list()
        pairs.append(items)

    def to_number(s):
        total = 0
        count = 1
        for ch in s:
            if ch == 'm':
                total += count * 1000
                count = 1
            elif ch == 'c':
                total += count * 100
                count = 1
            elif ch == 'x':
                total += count * 10
                count = 1
            elif ch == 'i':
                total += count
                count = 1
            else:
                count = int(ch)
        return total

    def from_number(num):
        result = ''
        if num >= 1000:
            k = num // 1000
            if k > 1:
                result += str(k)
            result += 'm'
            num = num % 1000
        if num >= 100:
            k = num // 100
            if k > 1:
                result += str(k)
            result += 'c'
            num = num % 100
        if num >= 10:
            k = num // 10
            if k > 1:
                result += str(k)
            result += 'x'
            num = num % 10
        if num >= 1:
            k = num
            if k > 1:
                result += str(k)
            result += 'i'
        return result

    for s, t in pairs:
        total = to_number(s) + to_number(t)
        roman = from_number(total)
        results.append(roman)
    print('\n'.join(results))

main()