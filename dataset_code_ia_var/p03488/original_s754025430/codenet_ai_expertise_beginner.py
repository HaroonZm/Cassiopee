import sys

def read_input():
    s = sys.stdin.readline().strip()
    x, y = map(int, sys.stdin.readline().split())
    return s, x, y

def check_subset_sum(target, numbers):
    total = sum(numbers)
    t = (total + target) // 2
    if total == 0 and target == 0:
        return True
    if (total - target) % 2 != 0 or t < 0:
        return False
    dp = [False] * (t + 1)
    dp[0] = True
    for num in numbers:
        for j in range(t, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    return dp[t]

def main():
    s, x, y = read_input()
    s = s.replace('TF', 'T F')
    s = s.replace('FT', 'F T')
    parts = s.split()
    if parts[0][0] == 'F':
        x -= len(parts[0])
        parts = parts[1:]

    moves_x = []
    moves_y = []
    flag = 0
    for i in range(len(parts)):
        length = len(parts[i])
        if i % 2 == 0:
            last_length = length
        else:
            flag ^= last_length % 2
            if flag == 0:
                moves_x.append(length)
            else:
                moves_y.append(length)

    if check_subset_sum(x, moves_x) and check_subset_sum(y, moves_y):
        print('Yes')
    else:
        print('No')

main()