N = int(input())
ABC = [0]*5
for i in range(5):
  ABC[i] = int(input())
  
Amin = min(ABC)

if N%Amin ==0:
  ans = N//Amin-1+5
else:
  ans = N//Amin+5

print(ans)