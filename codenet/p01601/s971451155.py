def isPalindrome(n):
    s = str(n)
    return s == s[::-1]
n = input()
p = q = n
while isPalindrome(p)==False:
    p += 1
while isPalindrome(q)==False:
    q -= 1
print q if abs(n-q)<=abs(p-n) else p