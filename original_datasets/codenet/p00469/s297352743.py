import itertools

while(True):
  n = int(input())
  k = int(input())
  if (n,k) == (0,0):
    break
  num_lis = []
  for _ in range(n):
    num_lis.append(input())
  word_list = []
  
  for item in list(itertools.permutations(num_lis,k)):
    word_list.append("".join(item))
  
  print(len(set(word_list)))