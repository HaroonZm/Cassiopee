def convert(S):
    cur = 0
    def parse():
        nonlocal cur
        if S[cur] == ')':
            return ()
        cur += 1 # '('
        left = parse()
        cur += 2 # ')['
        num = 0
        while S[cur] != ']':
            num = 10*num + int(S[cur])
            cur += 1
        cur += 2 # ']('
        right = parse()
        cur += 1 # ')'
        return left, num, right
    return parse()
def dfs(A, B):
    if not A or not B:
        return ()
    return (dfs(A[0], B[0]), [A[1] + B[1]], dfs(A[2], B[2]))
print(str(dfs(convert(input()), convert(input()))).replace(", ","")[1:-1])