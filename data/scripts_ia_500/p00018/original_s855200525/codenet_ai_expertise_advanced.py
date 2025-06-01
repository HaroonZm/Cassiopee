def main():
    a = sorted(map(int, input().split()), reverse=True)
    print(*a)

if __name__ == "__main__":
    main()