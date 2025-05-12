from collections import Counter
input()
s = set(map(int,input().split()))
input()
print(Counter(n in s for n in map(int,input().split()))[True])