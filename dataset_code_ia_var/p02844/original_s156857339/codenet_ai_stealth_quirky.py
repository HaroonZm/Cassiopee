import sys

lambda_i = sys.stdin.readline

stuff = [set() for _ in range(3)]

(lambda s: [stuff[2].update({y + x for y in stuff[1]}) or stuff[1].update({y + x for y in stuff[0]}) or stuff[0].add(x) for x in s])(lambda_i().strip())

(lambda: print(len(stuff[2])))()