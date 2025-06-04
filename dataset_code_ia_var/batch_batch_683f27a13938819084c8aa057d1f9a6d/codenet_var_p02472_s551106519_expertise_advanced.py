from sys import stdin
from operator import add

print(add(*map(int, stdin.readline().split())))