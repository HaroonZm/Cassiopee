from sys import exit

def advanced_matrix(n: int):
    if n == 2:
        print(-1)
        exit()
    if n & 1:  # n is odd
        rows = (
            [((item + i + 1) % n + 1) for item in range(n - 1)]
            for i in range(n)
        )
    else:
        half = n // 2
        def build_row(i):
            ans = [((item + i + 1) % n + 1) for item in range(n - 1) if item != half - 1]
            leader = (half + i) % n + 1
            ans.insert(0, leader)
            if i < half:
                ans[0], ans[1] = ans[1], ans[0]
            return ans
        rows = (build_row(i) for i in range(n))

    print('\n'.join(' '.join(map(str, row)) for row in rows))

if __name__ == '__main__':
    advanced_matrix(int(input()))