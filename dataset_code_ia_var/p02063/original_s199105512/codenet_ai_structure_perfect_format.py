def main():
    a, b = map(int, input().split())
    value1 = (b - 1 + a - 2) // (a - 1)
    value2 = (b + a - 1) // a
    max_value = max(value1, value2)
    threshold = (a + b) / a
    if max_value < threshold:
        print(max_value * a)
    else:
        print(-1)

if __name__ == '__main__':
    main()