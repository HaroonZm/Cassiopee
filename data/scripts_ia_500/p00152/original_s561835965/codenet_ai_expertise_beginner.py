import sys

def bowling_score(data):
    name_id = data[0]
    data = data[1:]
    frame = 1
    scores = [0]*11
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

def main():
    while True:
        m = int(sys.stdin.readline())
        if m == 0:
            break
        results = []
        for _ in range(m):
            line = sys.stdin.readline()
            data = list(map(int, line.split()))
            name_id, score = bowling_score(data)
            results.append([-score, name_id])
        results.sort()
        for s, i in results:
            print(i, -s)

main()