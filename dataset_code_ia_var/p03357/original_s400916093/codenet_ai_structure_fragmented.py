from itertools import accumulate

def parse_input():
    n = int(input())
    rev = [[0] * n, [0] * n]
    for i in range(n * 2):
        c, a = input().split()
        a = int(a) - 1
        rev[int(c == 'B')][a] = i
    return n, rev

def create_acc_row(n2):
    return [0] * n2

def update_row(row, index):
    row[index] += 1
    return row

def accumulate_row(row):
    return list(accumulate(row))

def reverse_list(l):
    return list(reversed(l))

def process_x_entry(row, x, n2):
    index = n2 - x - 1
    row = update_row(row, index)
    acc_row = reverse_list(accumulate_row(row))
    return row, acc_row

def existence_right_single(n, rev_c):
    n2 = n * 2
    acc = []
    row = create_acc_row(n2)
    acc.append(list(row))
    for x in rev_c:
        row, acc_row = process_x_entry(row, x, n2)
        acc.append(acc_row)
    return acc

def existence_right_all(n, rev):
    return [existence_right_single(n, rev_c) for rev_c in rev]

def get_initial_dp(cost1, rev1):
    acc_values = (c[y] for y, c in zip(rev1, cost1))
    dp = [0] + list(accumulate(acc_values))
    return dp

def zip_rev_cost(rev0, cost0):
    for x, cw0, cw1 in zip(rev0, cost0, cost0[1:]):
        yield x, cw0, cw1

def zip_rev_cost_b(rev1, cost1):
    for b, (y, cb0, cb1) in enumerate(zip(rev1, cost1, cost1[1:])):
        yield b, y, cb0, cb1

def compute_ndp(n, dp, x, cw0, cw1, rev1, cost1):
    ndp = [0] * (n + 1)
    cw0x = cw0[x]
    ndp[0] = prev = dp[0] + cw0x
    for b, y, cb0, cb1 in zip_rev_cost_b(rev1, cost1):
        val1 = dp[b + 1] + cw0x + cb1[x]
        val2 = prev + cw1[y] + cb0[y]
        ndp[b + 1] = prev = min(val1, val2)
    return ndp

def full_dp(n, rev, cost):
    dp = get_initial_dp(cost[1], rev[1])
    for x, cw0, cw1 in zip_rev_cost(rev[0], cost[0]):
        dp = compute_ndp(n, dp, x, cw0, cw1, rev[1], cost[1])
    return dp[n]

def solve(n, rev):
    cost = existence_right_all(n, rev)
    return full_dp(n, rev, cost)

def main():
    n, rev = parse_input()
    result = solve(n, rev)
    print(result)

main()