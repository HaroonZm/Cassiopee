from functools import reduce

inputs = map(int, (input() for _ in range(4)))
total_minutes = reduce(int.__add__, inputs)
print(*divmod(total_minutes, 60), sep='\n')