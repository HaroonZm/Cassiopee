from collections import Counter

def resolve():
    n, k = map(int, input().split())
    a = map(int, input().split())
    freq = Counter(a)
    if len(freq) <= k:
        print(0)
        return
    excess = sum(v for v in sorted(freq.values())[:len(freq) - k])
    print(excess)

if __name__ == "__main__":
    resolve()