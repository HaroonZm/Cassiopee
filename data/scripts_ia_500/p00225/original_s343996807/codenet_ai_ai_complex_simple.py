from functools import reduce
ca = ord('a')
exec(reduce(lambda f,x: f+chr(10)+x,[
    "while 1:",
    " N = (lambda z:int(z))(input())",
    " if N==0:break",
    " G=list(map(lambda _:[],[None]*26))",
    " S,T=[0]*26,[0]*26",
    " exec(reduce(lambda a,b:a+chr(10)+b,map(lambda i:\"\"\"word=input()\ns=(ord(word[0])-ca)\nt=(ord(word[-1])-ca)\nS[s]+=1\nT[t]+=1\nG[s].append(t)\"\"\",range(N))))",
    " ok=(lambda S,T:all(map(lambda i:S[i]==T[i],range(26))))(S,T)",
    " que=(lambda q:exec(\"\"\"from collections import deque\nq=deque()\nU=[0]*26\nfor i in range(26):\n if S[i]:\n  q.append(i)\n  U[i]=1\n  break\nwhile q:\n v=q.popleft()\n for w in G[v]:\n  if U[w]:continue\n  U[w]=1\n  q.append(w)\"\"\",globals(),{'q':q})) or q)([])",
    " ok=ok and all([not S[i] or U[i] for i in range(26)])",
    " print(('NG','OK')[ok])"
]))