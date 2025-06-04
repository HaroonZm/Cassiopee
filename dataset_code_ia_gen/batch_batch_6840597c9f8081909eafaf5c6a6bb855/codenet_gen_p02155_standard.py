import sys
input = sys.stdin.readline

N,D = map(int,input().split())
a = list(map(int,input().split()))

def grundy(x,d):
    return x % (d+1)

xor_sum = 0
for length in a:
    xor_sum ^= grundy(length,D)

print("First" if xor_sum!=0 else "Second")