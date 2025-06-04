listmagic = lambda l: sum([int(a)%2 for a in l])>1 and "Hom" or "Tem"
from sys import stdin as _s
print(listmagic(_s.readline().split()))