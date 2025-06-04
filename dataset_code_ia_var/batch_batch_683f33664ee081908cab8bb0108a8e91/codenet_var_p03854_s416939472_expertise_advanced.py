import re

S = input()
pattern = re.compile(r'(eraser|erase|dreamer|dream)')

S = pattern.sub('', S)

print('YES' if not S else 'NO')