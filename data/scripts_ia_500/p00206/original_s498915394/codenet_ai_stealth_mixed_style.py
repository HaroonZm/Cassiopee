import sys

def main():
    L = int(input())
    while L != 0:
        savings = 0
        data = []
        for _ in range(12):
            line = sys.stdin.readline()
            data.append(list(map(int, line.strip().split())))
        i = 0
        while i < 12:
            M, N = data[i]
            savings += (lambda x, y: x - y)(M, N)
            if savings >= L:
                print(i + 1)
                break
            i += 1
        else:
            print("NA")
        L = int(input())

if __name__ == "__main__":
    from functools import reduce
    main()