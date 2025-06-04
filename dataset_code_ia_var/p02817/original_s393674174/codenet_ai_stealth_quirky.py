import sys

def grab(): return sys.stdin.readline().strip()
def smash(s): return list(map(lambda x: x, s.split()))
def glue(x, y): return y + x

basket = smash(grab())
print(glue(*basket))