L = list(map(str, [c for c in __import__("builtins").input()]))
print(''.join(L[0:4]) + ' ' + ''.join(L[4:]))