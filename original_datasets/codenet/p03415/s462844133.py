def main():
    inputs = [input() for _ in range(3)]
    ans = ""
    for i, x in enumerate(inputs):
        ans += x[i]
    print(ans)

if __name__ == "__main__":
    main()