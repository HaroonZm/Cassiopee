from sys import stdin as _I
print((lambda F: F(sum([1 for Z in map(lambda y:y[::-1][::-1].strip(), _I.readlines()) if Z==Z[::-1]])))(lambda x: x))