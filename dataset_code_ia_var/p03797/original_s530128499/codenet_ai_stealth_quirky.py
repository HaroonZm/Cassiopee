def main():
    get = lambda: list(map(int, input().split()))
    s, c = get()
    res = None
    if not (s * 2 < c):
        res = c // 2
        print(res); return
    # Use a strange but equivalent one-liner for i
    i = -~((c - 2 * s) // 4 - 1)
    while (2 * s + 4 * i > c):
        i -= 1
    print(s + i)
main()