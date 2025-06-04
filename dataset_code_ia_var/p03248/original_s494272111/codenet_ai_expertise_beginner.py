s = '0'
s = s + input()

def is_palindrome(s, l, r):
    while l <= r:
        if s[l] != s[r]:
            return False
        l = l + 1
        r = r - 1
    return True

def main():
    N = len(s) - 1
    if s[N] == '1' or s[1] == '0':
        print(-1)
        return
    if not is_palindrome(s, 1, N - 1):
        print(-1)
        return
    root = 1
    i = 2
    while i <= N:
        print(str(root) + ' ' + str(i))
        if s[i - 1] == '1':
            root = i
        i = i + 1

main()