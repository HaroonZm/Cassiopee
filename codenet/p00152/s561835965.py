"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0152

"""
import sys
from sys import stdin
input = stdin.readline

def bowling_score(data):
    name_id = data[0]
    data = data[1:]

    frame = 1
    scores = [0] * 11

    while frame <= 10:
        if data[0] == 10:
            scores[frame] = data[0] + data[1] + data[2]
            data = data[1:]
            frame += 1
        elif data[0] + data[1] == 10:
            scores[frame] = data[0] + data[1] + data[2]
            data = data[2:]
            frame += 1
        else:
            scores[frame] = data[0] + data[1]
            data = data[2:]
            frame += 1
    return name_id, sum(scores[1:])

def main(args):
    while True:
        m = int(input())
        if m == 0:
            break
        results = []
        for _ in range(m):
            data = [int(x) for x in input().split()]
            name_id, score = bowling_score(data)
            results.append([-score, name_id])

        results.sort()
        for s, i in results:
            print(i, -s)

if __name__ == '__main__':
    main(sys.argv[1:])