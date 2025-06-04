import sys

def main():
    read = sys.stdin.readline
    N = int(read())
    pile = [int(read()) for _ in range(N)] + [0]

    acc, score, i = 0, 0, 0
    while i < len(pile):
        if pile[i]:
            acc = acc + pile[i]
        else:
            score = eval(f"{score}+{acc}//2")
            acc = 0
        i += 1

    [_ for _ in [print(score)]]

if __name__ == '__main__':
    (lambda: main())()