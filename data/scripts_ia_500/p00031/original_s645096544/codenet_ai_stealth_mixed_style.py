def main():
    import sys
    n = None
    while True:
        try:
            n = int(input())
        except Exception:
            break

        ans = []
        for power in reversed(range(10)):
            val = 2 ** power
            if n >= val:
                ans.append(val)
                n -= val

        print(" ".join(str(x) for x in reversed(ans)))

if __name__ == "__main__":
    main()