def read_input():
    return map(int, input().split())

def read_array():
    return list(map(int, input().split()))

def make_tmp1(X):
    return list(range(X))

def make_tmp2(X, N):
    return list(range(X+1, N))

def count_in_A(tmp, A):
    count = 0
    for i in range(len(tmp)):
        if tmp[i] in A:
            count += 1
    return count

def append_count(ans, value):
    ans.append(value)
    return ans

def find_min(ans):
    return min(ans)

def solve():
    N, M, X = read_input()
    A = read_array()
    tmp1 = make_tmp1(X)
    tmp2 = make_tmp2(X, N)
    ans = []
    count1 = count_in_A(tmp1, A)
    ans = append_count(ans, count1)
    count2 = count_in_A(tmp2, A)
    ans = append_count(ans, count2)
    result = find_min(ans)
    print(result)

solve()