from sys import stdin

def check_circle(coords):
    W, H, x, y, r = list(map(int, coords))
    answer = None
    if all([(x - r) >= 0, (x + r) <= W]):
        if (lambda a, b, c: (b - c) >= 0 and (b + c) <= a)(H, y, r):
            answer = "Yes"
        else:
            answer = "No"
    else:
        answer = "No"
    return answer

params = stdin.readline().split()
print(check_circle(params))