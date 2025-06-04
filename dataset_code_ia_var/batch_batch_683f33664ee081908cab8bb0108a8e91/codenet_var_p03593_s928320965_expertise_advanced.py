from collections import Counter

def int_input():
    return int(input())

def list_int_input():
    return list(map(int, input().split()))

def read():
    H, W = map(int, input().split())
    count = Counter()
    for _ in range(H):
        count.update(input().strip())
    return H, W, count

def solve(H, W, count):
    vals = count.values()
    odd = sum(v % 2 for v in vals)
    pairs = sum((v // 2) % 2 for v in vals)
    quads = sum(v // 4 for v in vals)
    h_even = not H % 2
    w_even = not W % 2

    if h_even and w_even:
        return "Yes" if odd == 0 and sum(v // 4 * 4 for v in vals) == H * W else "No"
    elif h_even or w_even:
        side = H if w_even else W
        return "Yes" if odd == 0 and pairs <= side//2 else "No"
    else:
        return "Yes" if odd == 1 and pairs <= (H + W) // 2 - 1 else "No"

def main():
    params = read()
    print(solve(*params))

if __name__ == "__main__":
    main()