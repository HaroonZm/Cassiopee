def i_map():
    return map(int, input().split())

def main():
    a, b, c, d = i_map()
    res1 = a * c
    res2 = a * d
    res3 = b * c
    res4 = b * d
    ans = [res1, res2, res3, res4]
    print(max(ans))

if __name__ == "__main__":
    main()