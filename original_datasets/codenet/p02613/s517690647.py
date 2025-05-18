def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from collections import  Counter
N = INT()
S = [input() for _ in range(N)]

S = Counter(S)
print(f"AC x {S['AC']}")
print(f"WA x {S['WA']}")
print(f"TLE x {S['TLE']}")
print(f"RE x {S['RE']}")