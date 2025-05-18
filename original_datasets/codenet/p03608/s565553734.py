#!/usr/bin/python

import itertools
import sys

def main(argv):
    line = sys.stdin.readline()
    while line:
        N, M, R = map(lambda x: int(x), line.split(" ", 3))
        r  = map(lambda x: int(x) - 1, sys.stdin.readline().split(" "))
        weights = [[0 for i in xrange(N)] for j in xrange(N)]
        for i in xrange(M):
            a, b, c = map(lambda x: int(x), sys.stdin.readline().split(" ", 3))
            weights[a - 1][b - 1] = c
            weights[b - 1][a - 1] = c

        for k in xrange(N):
            for i in xrange(N):
                for j in xrange(N):
                    if j > i:
                        if weights[i][k] > 0 and weights[k][j] > 0:
                            length = weights[i][k] + weights[k][j]
                            if weights[i][j] == 0 or weights[i][j] > length:
                                weights[i][j] = length
                                weights[j][i] = length

        min_length = -1
        for p in itertools.permutations(r):
            length = 0
            previous = p[0]
            for i in p[1:]:
                length += weights[previous][i]
                previous = i
            if min_length == -1:
                min_length = length
            elif min_length > length:
                min_length = length
        print min_length

        line = sys.stdin.readline()

if __name__ == "__main__":
    main(sys.argv)