from bisect import bisect
readline = open(0).readline
N = int(readline())
*A, = map(int, readline().split())
open(1, 'w').writelines(["%d\n" % bisect(A, int(readline())-1) for q in range(int(readline()))])