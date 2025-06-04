value_first, value_second = map(int, input().split())
concat_first = 0
concat_second = 0
for index_first in range(value_second):
    concat_first += value_first * (10 ** index_first)
for index_second in range(value_first):
    concat_second += value_second * (10 ** index_second)
if value_first < value_second:
    print(concat_first)
elif value_first > value_second:
    print(concat_second)
else:
    print(min(concat_first, concat_second))