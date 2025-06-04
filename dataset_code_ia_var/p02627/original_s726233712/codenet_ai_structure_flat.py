import re
a = input()
pattern = '[A-Z]'
if re.match(pattern, a):
    print("A")
else:
    print("a")