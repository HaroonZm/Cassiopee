from functools import reduce
from operator import add

def main():
    _, S = map(lambda f: f(), (lambda: int(input()), input))
    ans = reduce(add, map(lambda i: S[i:i+3] == 'ABC', range(len(S) - 2)), 0)
    print(ans)

if __name__ == '__main__':
    (lambda f: f())(main)