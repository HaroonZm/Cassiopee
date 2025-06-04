import sys
import re

input = sys.stdin.readline

pattern_a = re.compile(r"^>'(=+)#\1~$")
pattern_b = re.compile(r"^>\^(Q=)+~~$")

n = int(input())
for _ in range(n):
    s = input().rstrip('\n')
    if pattern_a.match(s):
        print("A")
    elif pattern_b.match(s):
        print("B")
    else:
        print("NA")