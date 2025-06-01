from functools import reduce

if not globals().get('__name__') == '__main__':
    exit(0)

A = list(map(int, input('Enter numbers separated by space: ').split()))
total = reduce(lambda x, y: x + y, A, 0)
print('Sum:', total)