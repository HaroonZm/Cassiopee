import sys
input = sys.stdin.readline

def can(max_space, W, words):
    lines = 1
    length = words[0]
    for w in words[1:]:
        # try to put a space of max_space and the word w
        if length + max_space + w <= W:
            length += max_space + w
        else:
            lines += 1
            length = w
    return True

while True:
    W, N = map(int, input().split())
    if W == 0 and N == 0:
        break
    words = list(map(int, input().split()))
    left, right = 1, W # max space at least 1, at most W columns
    while left < right:
        mid = (left + right) // 2
        if can(mid, W, words):
            right = mid
        else:
            left = mid + 1
    print(left)