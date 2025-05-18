n = raw_input()
l1 = [int(x) for x in raw_input().split()]
n = raw_input()
print len(set(l1) & set([int(y) for y in raw_input().split()]))