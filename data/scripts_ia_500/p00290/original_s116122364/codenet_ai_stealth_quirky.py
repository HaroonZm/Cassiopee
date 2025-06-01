_ = lambda __, ___: int(___)
a, b = map(_, input().split(), (None, None))
print(eval(f'{a}*{b}'))