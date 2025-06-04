def main():
    import sys
    # Precompute maximum number of carbons for longest chain lengths 1 to 30
    max_carbons = [0]*31
    max_carbons[1] = 1
    for i in range(2,31):
        max_carbons[i] = max_carbons[i-1] + 2*(i-1)
    for line in sys.stdin:
        n = line.strip()
        if not n.isdigit():
            continue
        n = int(n)
        print(max_carbons[n])
if __name__=="__main__":
    main()