from itertools import accumulate
n = int(input())
a_list = list(map(int,input().split()))
cumsum = list(accumulate(a_list))
num_dict = {0:1}
for s in cumsum :
  if s in num_dict.keys():
    num_dict[s] += 1
  else:
    num_dict[s] = 1

res = 0
for val in num_dict.values():
  res += val * (val - 1)//2
  
print(res)