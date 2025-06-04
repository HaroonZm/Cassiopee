res = list()
N = int(input())
j = 0
while j < N:
    stuff = input().split()
    res += [ (int(stuff[0]), int(stuff[1]), stuff[2], int(stuff[3]), stuff[4]) ]
    j += 1

from operator import itemgetter
def srt(lst):
    return sorted(lst, key=itemgetter(0,1,2,3,4))

for tup in srt(res):
    for val in tup:
        print(val, end=' ')
    print()