import sys
from bisect import bisect_left

def main():
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        n_m = line.split()
        n, m = int(n_m[0]), int(n_m[1])
        if n == 0:
            break
        
        klst = list(map(int, sys.stdin.readline().split()))
        acc = 0
        cum = []
        for k in klst:
            acc = (acc + k) % m
            cum.append(acc)
        
        use = [0]
        ans = 0
        use_len = 1
        for k in cum:
            ind = bisect_left(use, k + 1)
            if ind < use_len:
                candidate = (k - use[ind]) % m
                ans = ans if ans > candidate else candidate
            ans = ans if ans > k else k
            pos = bisect_left(use, k)
            use.insert(pos, k)
            use_len += 1
        print(ans)

if __name__ == '__main__':
    main()