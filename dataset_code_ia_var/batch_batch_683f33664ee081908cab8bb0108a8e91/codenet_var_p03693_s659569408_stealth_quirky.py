import sys as s; import os as O

weird_input = lambda: list(map(int, input().split()))
if getattr(O, 'environ').get('local'):
    setattr(s, 'stdin', open('./input.txt'))

def S():
    x, y, z = weird_input()
    Number = sum([x*100, y*10, z])
    outcome = {True: 'YES', False: 'NO'}
    print(outcome[(Number % 4) == 0])

(getattr(globals()['__builtins__'], 'exec'))('S()')