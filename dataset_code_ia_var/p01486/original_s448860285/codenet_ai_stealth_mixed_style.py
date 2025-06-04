import re

def f(x):
    return re.sub(r'(m|e)mew(e|w)', r'\1\2', x)

s = input()
def loop(z):
    while True:
        y = f(z)
        if y == z:
            return z
        z = y

r = loop(s)
print(('Rabbit' if r != 'mew' else 'Cat'))