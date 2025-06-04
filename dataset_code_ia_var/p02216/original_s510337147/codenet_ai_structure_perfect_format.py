import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
import math

def getN():
    return int(input())

def getList():
    return list(map(int, input().split()))

INF = 10 ** 20

def main():
    n = getN()
    nums = getList()
    sm = sum(nums)
    ans = sm % 2
    if n % 2 == 1:
        if ans == 1:
            print("First")
        else:
            print("Second")
        return
    if n % 2 == 0:
        mn = min(nums)
        if ans == 1:
            if sm == mn * n:
                print("Second")
            else:
                print("First")
        else:
            if mn % 2 == 1:
                print("First")
            else:
                print("Second")

if __name__ == "__main__":
    main()