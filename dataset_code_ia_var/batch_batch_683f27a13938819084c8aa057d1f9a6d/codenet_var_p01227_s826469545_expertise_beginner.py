import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n_k = sys.stdin.readline().split()
        n = int(n_k[0])
        k = int(n_k[1])
        houses = list(map(int, sys.stdin.readline().split()))

        if k >= n:
            print(0)
            continue

        diffs = []
        for i in range(1, n):
            diff = houses[i] - houses[i-1]
            diffs.append((diff, i-1))

        diffs.sort(reverse=True)

        cut_points = []
        for j in range(k-1):
            cut_points.append(diffs[j][1]+1)  # where to cut

        cut_points.sort()

        total = 0
        start = 0
        for cut in cut_points:
            total += houses[cut-1] - houses[start]
            start = cut
        total += houses[n-1] - houses[start]

        print(total)

if __name__ == '__main__':
    main()