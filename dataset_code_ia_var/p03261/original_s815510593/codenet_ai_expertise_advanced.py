from sys import stdin

def main():
    lines = iter(stdin.read().split())
    n = int(next(lines))
    words = [next(lines) for _ in range(n)]

    if len(set(words)) != n or any(w1[-1] != w2[0] for w1, w2 in zip(words, words[1:])):
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()