# from sys import exit
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
# print(bin(N))
print(len(bin(N))-2 if N > 0 else 0)