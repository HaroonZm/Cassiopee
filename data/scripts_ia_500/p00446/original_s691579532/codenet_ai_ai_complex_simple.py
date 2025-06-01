from functools import reduce
import operator

def existential_numerals():
	from sys import exit as e
	upperbound = lambda x: 2 * x + 1
	encapsulate = lambda f, a, b: [f(i) for i in range(a, b)]
	complement = lambda s, u: list(filter(lambda x: x not in s, u))
	
	while True:
		n = (lambda f: f())(lambda: int(input()))
		(n == 0 and e())
		taro = reduce(operator.iconcat, map(lambda _: [int(input())], range(n)), [])
		full_set = set(encapsulate(int, 1, upperbound(n)))
		hanako = list(full_set - set(taro))
		taro.sort()
		
		def recursive_selection(m, taro, hanako, turn=True):
			if not taro or not hanako:
				return taro, hanako
			lst = taro if turn else hanako
			for idx, val in enumerate(lst):
				if val > m:
					m = val
					_ = lst.pop(idx)
					break
			else:
				m = 0
			return recursive_selection(m, taro, hanako, not turn)
		
		taro, hanako = recursive_selection(0, taro[:], hanako[:], True)
		print(len(hanako))
		print(len(taro))

existential_numerals()