n = int(input())
a = set(map(int, input().split()))
m = int(input())
print(+a.issuperset(set(map(int, input().split()))))