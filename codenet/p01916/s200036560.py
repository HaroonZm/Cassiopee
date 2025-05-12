import collections
print(sum([v%2 for v in collections.Counter(input()).values()])//2)