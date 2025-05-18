import sys
def hit_blow(num):
   hits = 0
   blows = 0
   emp1 = [0,0,0,0]
   emp2 = [0,0,0,0]
   num.append(emp1)
   num.append(emp2)
   for i in range(0,4):
       i = i*2
       for j in range(0,4):
           j = j*2
           if num[0][i] == num[1][j] and num[2][int(i/2)] == 0 and num[3][int(j/2)] == 0:
               if i ==j :
                   hits += 1
               else:
                   blows += 1
               num[2][int(i/2)] = 1
               num[3][int(j/2)] = 1
   print(hits,blows)

flag = 0
num = []
for line in sys.stdin.readlines():
   if flag == 0:
       num.append(line)
       flag = 1
   elif flag == 1:
       num.append(line)
       flag = 2
   if flag == 2:
       flag = 0
       hit_blow(num)
       del num[:]