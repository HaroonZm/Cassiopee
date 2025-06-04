import re

S = input()
pattern = re.compile(r'^(dream(er)?|erase(r)?)+$')
print("YES" if pattern.fullmatch(S) else "NO")