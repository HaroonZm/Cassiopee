def main():
    i = 0
    while True:
        try:
            n = int(raw_input())
            result = []
            for bit in range(10):
                if (n >> bit) & 1:
                    result.append(str(1 << bit))
            print ' '.join(result)
        except EOFError:
            break

if __name__ == '__main__':
    main()