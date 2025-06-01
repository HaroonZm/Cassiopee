import sys
def main():
    while True:
        s = int(sys.stdin.readline())
        if not s:
            return
        values = []
        for _ in range(9):
            values.append(int(sys.stdin.readline()))
        print(s - sum(values))

if __name__ == "__main__":
    main()