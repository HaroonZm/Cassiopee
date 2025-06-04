from functools import reduce

def get_char(x, i):
    return x[i]

a = input()
b = input()
c = input()

inputs = [a, b, c]
indices = (0, 1, 2)

chars = []
for idx, s in zip(indices, inputs):
    chars.append(get_char(s, idx))

print(reduce(lambda x, y: x + y, chars))