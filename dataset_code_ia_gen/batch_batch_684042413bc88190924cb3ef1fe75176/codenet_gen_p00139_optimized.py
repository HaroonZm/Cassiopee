import sys
import re

input = sys.stdin.readline

pattern_A = re.compile(r"^>'(=+)#\1~$")
pattern_B = re.compile(r"^>\^((Q=)+)~~$")

n = int(input())
for _ in range(n):
    s = input().rstrip('\n')
    if pattern_A.match(s):
        print("A")
    elif pattern_B.match(s):
        print("B")
    else:
        print("NA")