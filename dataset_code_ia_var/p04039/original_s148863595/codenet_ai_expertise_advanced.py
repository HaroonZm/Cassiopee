from sys import stdin

def main():
    N, K = stdin.readline().split()
    D = set(stdin.readline().split())
    allowed = {str(d) for d in range(10)} - D

    n = int(N)
    allowed_check = allowed.__contains__
    while True:
        if all(allowed_check(ch) for ch in str(n)):
            print(n)
            return
        n += 1

if __name__ == '__main__':
    main()