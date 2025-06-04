def main():
    import sys
    fib = [0, 1, 2, 4] + [0]*27
    for i in range(4, 31):
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3]
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        total_ways = fib[n]
        days = (total_ways + 9) // 10
        years = (days + 364) // 365
        print(years)
if __name__ == "__main__":
    main()