n = int(input())
s = input()
k = int(input())
c = s[k - 1]

print(''.join(c if ch == c else '*' for ch in s))