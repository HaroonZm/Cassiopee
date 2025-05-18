#!/usr/bin/python

import sys

def main(argv):
    line = sys.stdin.readline()
    while line:
        N, M = map(lambda x: int(x), line.split(" ", 2))

        services_1 = {}
        services_n = []
        for i in xrange(M):
            a, b = map(lambda x: int(x), sys.stdin.readline().split(" ", 2))
            if a == 1:
                services_1[b] = True
            if b == N:
                services_n.append(a)

        if 1 in services_n:
            print("POSSIBLE")

        result = "IMPOSSIBLE"
        for service in services_n:
            if service == 1 or service in services_1:
                result = "POSSIBLE"
                break
        print result                

        line = sys.stdin.readline()

if __name__ == "__main__":
    main(sys.argv)