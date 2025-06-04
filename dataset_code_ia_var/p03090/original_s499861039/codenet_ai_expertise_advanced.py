from sys import stdin, stdout

def main():
    N = int(stdin.readline())
    even = N % 2 == 0
    M = N * (N - 1) // 2 - (N // 2 if even else (N - 1) // 2)
    s = N + 1 if even else N
    pairs = (f"{i} {j}" for i in range(1, N) for j in range(i + 1, N + 1) if i + j != s)
    stdout.write(f"{M}\n" + "\n".join(pairs) + "\n")

if __name__ == "__main__":
    main()