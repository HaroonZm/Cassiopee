N, M = list(map(int, input().split()))

exe_time = 1900 * M + 100 * (N - M)
exe_time_exp = exe_time * pow(2, M)

print(exe_time_exp)