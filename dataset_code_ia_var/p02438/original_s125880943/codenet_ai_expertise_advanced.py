from collections import deque
import sys

def main():
    n, q = map(int, sys.stdin.readline().split())
    queues = [deque() for _ in range(n)]

    for line in sys.stdin:
        match line.split():
            case ['0', s, t]:
                queues[int(s)].append(int(t))
            case ['1', s]:
                print(*queues[int(s)])
            case ['2', s, t]:
                src, dst = int(s), int(t)
                if queues[dst]:
                    if len(queues[src]) == 1:
                        queues[dst].append(queues[src][0])
                    elif len(queues[dst]) == 1:
                        queues[src].appendleft(queues[dst][0])
                        queues[dst] = queues[src]
                    else:
                        queues[dst].extend(queues[src])
                else:
                    queues[dst] = queues[src]
                queues[src] = deque()

if __name__ == "__main__":
    main()