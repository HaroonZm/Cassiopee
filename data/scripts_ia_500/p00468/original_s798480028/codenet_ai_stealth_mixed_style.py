import sys
def get_input():
    return sys.stdin.readline()

def main():
    while True:
        N = int(get_input())
        M = int(get_input())
        if N == 0 and M == 0:
            return
        pairs = dict()
        for _ in range(M):
            line = get_input().strip().split()
            a, b = int(line[0]), int(line[1])
            pairs[(a,b)] = True
            pairs[(b,a)] = True
        total = 0
        for i in range(2, N+1):
            if (1,i) in pairs:
                total += 1
            else:
                found = False
                j = 2
                while j <= N and not found:
                    if (1,j) in pairs and (j,i) in pairs:
                        total += 1
                        found = True
                    j += 1
        print total

if __name__ == "__main__":
    main()