from itertools import accumulate

N = int(input())
S = input()

translate = {'I': 1, 'D': -1}
cummax = lambda it: accumulate(it, func=lambda a, b: max(a, b))

result = max(cummax(accumulate(map(translate.get, S), initial=0)))
print(result)