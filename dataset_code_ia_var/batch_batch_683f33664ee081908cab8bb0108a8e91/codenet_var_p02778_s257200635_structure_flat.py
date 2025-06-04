import re

S = input()

_result = re.sub('[a-z]', 'x', S)
print(_result)