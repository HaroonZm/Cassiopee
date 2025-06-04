def answerNumber(n):
 num1 = sorted(n)
 num2 = list(n)
 num2.sort(reverse=True)
 res_min = sum(val*(10**idx) for idx, val in enumerate(num2))
 res_max = 0
 i=0
 while i<len(n):
  res_max += num1[i]*(10**i)
  i+=1
 return res_min - res_max

rep = int(input())
indice = 0
while indice < rep:
 arr = []
 for d in input(): arr.append(int(d))
 print(answerNumber(arr))
 indice +=1