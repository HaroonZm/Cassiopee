def solve():
    s = input()
    lens = len(s)
    for i in range(1, lens // 2):
        sub = lens - 2 * i
        if s[:sub // 2] == s[sub//2:sub]:
            print(sub)
            break
if __name__ == "__main__":
    solve()