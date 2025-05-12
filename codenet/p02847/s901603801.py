S = input() 
D = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
C=0
for i in D :
    Ans = 7 - C
    if i == S : print(Ans)
    C += 1