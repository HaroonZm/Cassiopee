import sys

def solve(target_name, n):
    ans = 0
    for _ in range(n):
        signboard = input()
        found = False
        for st in [i for i, ch in enumerate(signboard) if ch == target_name[0]]:
            if found:
                break
            gap = 1
            while True:
                x = signboard[st::gap]
                if len(x) < len(target_name):
                    break
                if x.startswith(target_name):
                    found = True
                    break
                gap += 1
        ans += found
    return ans

def main(args):
    n = int(input())
    s = input()
    ans = solve(s, n)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])