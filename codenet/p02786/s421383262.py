import math
n = int(input())
n_log = math.log(n,2)
n_log_2 = math.floor(n_log)
print(2**(n_log_2+1)-1)