from functools import reduce
Str = input()
swap_map = {'1': ' ', '9': '1', ' ': '9'}
Str = ''.join(map(lambda c: reduce(lambda acc, k: swap_map[k] if c == k else acc, swap_map, c), Str))
print(Str)