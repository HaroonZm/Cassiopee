from collections import Counter

def main():
    counts = Counter(map(int, input().split()))
    print('YES' if counts == Counter({5:2, 7:1}) else 'NO')

main()