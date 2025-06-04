from sys import stdin

def main():
    t1, t2, r1, r2 = map(int, stdin.readline().split())
    result = (
        'Draw'
        if (r1, r2) == (-1, -1) and t1 == t2 or r1 == r2
        else
        'Alice' if (r1, r2) == (-1, -1) and t1 < t2 or r1 > r2
        else
        'Bob'
    )
    print(result)

main()