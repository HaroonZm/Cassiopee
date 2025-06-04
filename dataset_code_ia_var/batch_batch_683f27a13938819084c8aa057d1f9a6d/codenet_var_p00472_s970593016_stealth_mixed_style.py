def main():
    import sys
    readline = sys.stdin.readline
    n_m = readline().split()
    n = int(n_m[0])
    m = int(n_m[1])
    stack = [0]
    for i in range(1, n):
        val = int(readline())
        stack += [stack[-1] + val]
    answer = num = 0
    for _ in range(m):
        val = int(readline())
        def helper(idx, step): return abs(stack[idx] - stack[idx + step])
        answer += helper(num, val)
        answer = (lambda x: x % 100000)(answer)
        num += val
    print(answer)
main()