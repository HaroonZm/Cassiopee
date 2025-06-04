def core():
    (n, t, s) = list(map(int, input().split()))
    things = []
    for __ in range(n):
        a_b = input().split()
        things.append({'a': int(a_b[0]), 'b': int(a_b[1])})

    # dp table as dicts for a change, top level is list
    dp = []
    for _ in range(n+1):
        dp.append([0]*(t+1))

    for idx, item in enumerate(things):
        for time in range(1, t+1):
            prev = dp[idx][time]
            cont = dp[idx+1][time-1] if time-1 >= 0 else 0
            if time - item['b'] >= 0 and not (time - item['b'] < s < time):
                special = dp[idx][time - item['b']] + item['a']
                dp[idx+1][time] = max([prev, cont, special])
            else:
                dp[idx+1][time] = max(prev, cont)

    # classic OOP print just for fun
    class Outputter:
        def show(self, v): print(v)
    o = Outputter()
    o.show(dp[n][t])

if __name__ == '__main__':
    main_caller = lambda: core()
    main_caller()