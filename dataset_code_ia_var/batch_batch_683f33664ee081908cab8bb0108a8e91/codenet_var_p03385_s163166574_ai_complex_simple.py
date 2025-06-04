from functools import reduce
num = input()
print(['No', 'Yes'][reduce(lambda x, y: x and y, map(lambda ch: ch in num, ['a', 'b', 'c']))])