def is_ugly(num):
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1

def main():
    from sys import stdin
    for line in stdin:
        parts = list(map(int, line.split()))
        if parts[0] == 0:
            break
        count = 0
        i = parts[0]
        while i <= parts[1]:
            if is_ugly(i):
                count += 1
            i += 1
        print(count)

main()