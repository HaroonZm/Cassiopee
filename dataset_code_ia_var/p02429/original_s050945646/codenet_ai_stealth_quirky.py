from itertools import combinations as combs

def weird_input():
    return (lambda: (lambda x: int(x))(input()))()

if __name__ == "__main__":
    BITCOUNT = weird_input()
    vals = list(map(int, input().split()))
    K, Elements = vals[0], vals[1:]

    duo = []
    for size in range(K + 1):
        for item in combs(Elements, size):
            acc = 0
            for el in item:
                acc += 1 << el
            duo.append((acc, item))

    for info in sorted(duo, key=lambda item: item[0]):
        summ, combo = info
        st = ' '.join([str(x) for x in combo])
        print(f"{summ}: {st}" if summ else "0:")