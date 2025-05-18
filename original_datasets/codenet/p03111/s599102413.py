a, b, c, l_list = 0, 0, 0, []

def dfs(l_key, a_sum, b_sum, c_sum):
    if l_key == len(l_list):
        if min(a_sum, b_sum, c_sum) > 0:
            return abs(a - a_sum) + abs(b - b_sum) + abs(c - c_sum) - 30
        else:
            return 1 << 20

    l_value = l_list[l_key]
    ret0 = dfs(l_key + 1, a_sum, b_sum, c_sum)
    ret1 = dfs(l_key + 1, a_sum + l_value, b_sum, c_sum) + 10
    ret2 = dfs(l_key + 1, a_sum, b_sum + l_value, c_sum) + 10
    ret3 = dfs(l_key + 1, a_sum, b_sum, c_sum + l_value) + 10

    return min(ret0, ret1, ret2, ret3)

def main():
    global a, b, c, l_list

    n, a, b, c = map(int, input().split())
    l_list = [int(input()) for _ in range(n)]

    ans = dfs(0, 0, 0, 0)
    print(ans)

main()