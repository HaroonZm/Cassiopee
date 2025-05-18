readline = open(0).readline
N = int(readline())
A = set(map(int, readline().split()))
M = int(readline())
B = set(map(int, readline().split()))
print(+(len(A & B) == M))