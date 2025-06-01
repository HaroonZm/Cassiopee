from collections import Counter

def main():
    while True:
        n = int(input())
        if not n:
            break
        seq = list(map(int, input().split()))
        prev = seq[:]
        count = 0
        while True:
            freq = Counter(prev)
            new_seq = list(map(freq.get, prev))
            if new_seq == prev:
                break
            prev = new_seq
            count += 1
        print(count)
        print(*prev)

if __name__ == "__main__":
    main()