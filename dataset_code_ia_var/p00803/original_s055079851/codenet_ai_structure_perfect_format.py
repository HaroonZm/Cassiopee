cube = []
tetrahedral = []

def solve(n):
    min_sum = 0
    min_diff = 10 ** 6
    for i in cube:
        for j in tetrahedral:
            sum_value = i + j
            current_diff = n - sum_value
            if 0 <= current_diff < min_diff:
                min_diff = current_diff
                min_sum = sum_value
    return min_sum

if __name__ == '__main__':
    for i in range(0, 55):
        cube.append(i ** 3)
    for i in range(0, 97):
        tetrahedral.append(i * (i + 1) * (i + 2) // 6)
    ans = []
    while True:
        n = int(input())
        if n == 0:
            break
        ans.append(solve(n))
    print(*ans, sep='\n')