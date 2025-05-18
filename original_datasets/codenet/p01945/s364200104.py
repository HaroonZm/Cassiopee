s = input()
while '()' in s:
    s = s.replace('()', '')
else:
    print(s.count('('))