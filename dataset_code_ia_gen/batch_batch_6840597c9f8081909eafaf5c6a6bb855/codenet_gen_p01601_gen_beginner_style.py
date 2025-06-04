n = int(input())

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

closest = None
min_diff = None

for candidate in range(0, 100000):
    if is_palindrome(candidate):
        diff = abs(candidate - n)
        if min_diff is None or diff < min_diff or (diff == min_diff and candidate < closest):
            closest = candidate
            min_diff = diff

print(closest)