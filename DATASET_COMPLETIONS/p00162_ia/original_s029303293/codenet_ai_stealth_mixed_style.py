from math import log
def count_special(m, n):
    c = 0
    i = 0
    while i <= int(log(n,2))+1:
        j = 0
        while j <= int(log(n,3))+1:
            k = 0
            while k <= int(log(n,5))+1:
                val = pow(2,i)*pow(3,j)*pow(5,k)
                if val >= m and val <= n:
                    c += 1
                k += 1
            j += 1
        i += 1
    return c

def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            parts = line.split()
            m, n = int(parts[0]), int(parts[1])
            print(count_special(m,n))
        except (ValueError, IndexError):
            break

if __name__ == "__main__":
    main()