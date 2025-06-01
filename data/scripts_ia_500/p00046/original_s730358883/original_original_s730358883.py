import sys
def main():
    m = [] #mountain

    for line in sys.stdin:
        m.append(float(line))

    m.sort()

    ans = m[-1] - m[0]
    print(ans)

if __name__ == "__main__":
    main()