def main():
    while True:
        n_m = input()
        n, m = map(int, n_m.split())
        if n == 0:
            break
        ofuton = list(map(int, input().split()))
        dlst = list(map(int, input().split()))
        dlst.sort()

        INF = 10 ** 20
        end = 2 ** n - 1
        memo = {}

        def min_score(state, power, index):
            if state in memo:
                return memo[state]
            if state == end:
                return 0

            result = INF
            for i in range(n):
                mask = 1 << i
                if state & mask:
                    continue
                new_power = power + ofuton[i]
                new_state = state | mask

                # Find index in dlst where value just greater than new_power
                new_index = -1
                for k in range(m):
                    if dlst[k] > new_power:
                        break
                    new_index = k

                add = (m - new_index - 1) * ofuton[i]
                for j in range(index + 1, new_index + 1):
                    left = power
                    right = new_power
                    diff1 = new_power - dlst[j]
                    diff2 = dlst[j] - power
                    if diff1 < diff2:
                        add += diff2 - diff1
                res = -add + min_score(new_state, new_power, new_index)
                if res < result:
                    result = res
            memo[state] = result
            return result

        total = 0
        for d in dlst:
            total += d
        ans = total + min_score(0, 0, -1)
        print(ans)

main()