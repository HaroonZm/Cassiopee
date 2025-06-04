from functools import reduce
from itertools import starmap, cycle, islice, chain

num = input()

digitSum = lambda n: reduce(lambda x,y: x+y, chain.from_iterable(starmap(lambda a, b: [int(a)], zip(str(n), cycle([None])))))

print(*("No", "Yes")[digitSum(num).__mod__(9) == 0], sep='')