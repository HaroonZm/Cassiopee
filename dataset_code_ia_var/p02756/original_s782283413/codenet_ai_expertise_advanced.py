from collections import deque
import sys

def main():
    S = deque(sys.stdin.readline().strip())
    Q = int(sys.stdin.readline())
    reversed_flag = False

    for _ in range(Q):
        inp = sys.stdin.readline().split()
        if inp[0] == "1":
            reversed_flag = not reversed_flag
        else:
            F, C = int(inp[1]), inp[2]
            if (F == 1) ^ reversed_flag:
                S.appendleft(C)
            else:
                S.append(C)

    output = ''.join(reversed(S)) if reversed_flag else ''.join(S)
    print(output)

if __name__ == "__main__":
    main()