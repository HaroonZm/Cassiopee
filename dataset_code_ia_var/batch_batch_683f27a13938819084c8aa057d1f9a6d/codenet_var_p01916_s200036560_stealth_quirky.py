import collections as c
input_ = lambda : __import__('builtins').input()
c0unter = c.Counter(input_())
odd = list(map(lambda v: v & 1, c0unter.values()))
result = -(-sum(odd)//2) if sum(odd)%2 == 1 else sum(odd)//2
print(result)