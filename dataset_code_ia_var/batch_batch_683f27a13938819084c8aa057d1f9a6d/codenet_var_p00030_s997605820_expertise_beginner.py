import sys
sys.setrecursionlimit(10000)

def solve(i, current_sum, used_count):
    global count, target_sum, max_numbers
    if current_sum == target_sum and used_count == max_numbers:
        count += 1
        return
    if used_count > max_numbers or i == 10 or current_sum > target_sum:
        return
    solve(i + 1, current_sum, used_count)
    solve(i + 1, current_sum + i, used_count + 1)

while True:
    n_s = raw_input()
    n, s = map(int, n_s.split())
    if n == 0 and s == 0:
        break
    count = 0
    target_sum = s
    max_numbers = n
    solve(0, 0, 0)
    print count