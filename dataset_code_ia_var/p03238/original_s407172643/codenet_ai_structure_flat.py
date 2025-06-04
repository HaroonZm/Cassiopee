from sys import stdin

input = lambda: stdin.readline()

N = int(input())
if N < 2:
    print('Hello World')
else:
    A = int(input())
    B = int(input())
    print(A + B)