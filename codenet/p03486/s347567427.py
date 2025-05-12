s = input()
t = input()
List=[]
ListS= list(s)
ListT = list(t)
ListS.sort()
ListT.sort(reverse= True)
S = ""
T = ""
for i in range(len(ListS)):
  S += ListS[i]  
for i in range(len(ListT)):
  T += ListT[i]
if S == T:
  print("No")
else:
  List.append(S)
  List.append(T)
  List.sort()
  if List[0]==S:
    print("Yes")
  else:
    print("No")