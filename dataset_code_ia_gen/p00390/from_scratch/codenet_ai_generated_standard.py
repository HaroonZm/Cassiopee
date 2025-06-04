from itertools import permutations

def main():
    N = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    min_frustration = float('inf')
    for order in permutations(range(N)):
        total = 0
        for i in range(N):
            curr = order[i]
            right = order[(i+1)%N]
            left = order[(i-1)%N]
            if a[curr] == 0:  # right-handed
                if a[right] == 1:
                    total += w[curr]
            else:  # left-handed
                if a[left] == 0:
                    total += w[curr]
            if total >= min_frustration:
                break
        min_frustration = min(min_frustration, total)
    print(min_frustration)

if __name__ == '__main__':
    main()