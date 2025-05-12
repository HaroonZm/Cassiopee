from collections import defaultdict
from collections import deque
import itertools
import math

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

n,a,b = readInts()
print(max(0,(b-a)*(n-2)+1))