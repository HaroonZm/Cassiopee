from itertools import count

def process_sequence():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            b = list(map(int, input().split()))
            for cnt in count(0):
                if cnt > 10000:
                    print(-1)
                    break
                if b and b[0] == 1 and all(x2 - x1 == 1 for x1, x2 in zip(b, b[1:])):
                    print(cnt)
                    break
                b = [x - 1 for x in b]
                b.append(len(b))
                b = [x for x in b if x != 0]
        except EOFError:
            break

process_sequence()