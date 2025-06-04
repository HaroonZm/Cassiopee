def main():
    import sys
    # For n=1, max carbons is 1 (only one carbon)
    # For n >= 2, the formula is 2 * n (longest chain plus twice the branches on each internal carbon)
    # This corresponds to the largest compound with the longest chain n
    
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        n = int(line)
        if n == 1:
            print(1)
        else:
            print(2 * n)  # largest compound has 2*n carbons for longest chain length n


if __name__ == "__main__":
    main()