import sys as system

def solution(temps, garbs):
    collection = {}
    for i in range(len(temps)):
        collection[i] = sorted([cl[2] for cl in garbs if cl[0] <= temps[i] <= cl[1]])
    first, second = min(collection[0]), max(collection[0])
    dp = [[first, 0], [second, 0]]
    for idx in range(1, len(temps)):
        min_p = min(collection[idx])
        max_p = max(collection[idx])
        dp = [
            [min_p, max(dp[0][1] + abs(min_p - dp[0][0]), dp[1][1] + abs(min_p - dp[1][0]))],
            [max_p, max(dp[0][1] + abs(max_p - dp[0][0]), dp[1][1] + abs(max_p - dp[1][0]))]
        ]
    return max(dp[0][1], dp[1][1])

def run(params):
    d, n = [int(x) for x in input().split()]
    t_list = list(map(int, (input() for _ in range(d))))
    c_list = [list(map(int, input().split())) for _ in range(n)]
    answer = solution(t_list, c_list)
    print(answer)

if __name__ == "__main__":
    run(system.argv)