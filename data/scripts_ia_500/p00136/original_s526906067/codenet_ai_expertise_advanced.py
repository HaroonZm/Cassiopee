def main():
    from sys import stdin, stdout
    import itertools

    bins = [165, 170, 175, 180, 185]
    counts = [0] * (len(bins) + 1)

    n = int(stdin.readline())
    temps = (float(stdin.readline()) for _ in range(n))

    for temp in temps:
        idx = next((i for i, limit in enumerate(bins) if temp < limit), len(bins))
        counts[idx] += 1

    for i, count in enumerate(counts, 1):
        stdout.write(f"{i}:" + "*" * count + "\n")

if __name__ == "__main__":
    main()