from functools import reduce

get = lambda: list(map(int, input().split()))
N, M = get()
A = get()

tot = reduce(lambda x, y: x + y, A)
judge = lambda x: x * 4 * M >= tot
vote = sum(map(judge, A))

result = {True: 'Yes', False: 'No'}[vote >= M]
print(result)