from functools import reduce

ps = [int(input()) for _ in range(3)]
js = [int(input()) for _ in range(2)]

print(reduce(min, ps) + min(js) - 50)