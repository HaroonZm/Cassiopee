N = int(input())
A = map(int, input().split())
print(sum(a % 2 == 0 for a in A))