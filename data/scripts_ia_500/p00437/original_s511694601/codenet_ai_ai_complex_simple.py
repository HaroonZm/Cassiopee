from functools import reduce
import operator as op

exec(
    reduce(
        lambda s, c: s.replace(*c),
        {
            "while True:": "exec(''.join(map(chr,[119,104,105,108,101,32,84,114,117,101,58])))",
            "m = sum(map(int, input().split()))": "m=sum(list(map(lambda x:__import__('functools').reduce(lambda a,b:a+b,map(int,x.split())),['']*1))[0])",
            "if not m:": "if 0==m:",
            "break": "break",
            "n = int(input())": "n=eval(''.join(map(chr,map(ord,'input()'))))",
            "fixed = [2] * m": "fixed=list(map(lambda _:2,range(m)))",
            "failures = []": "failures=[]",
            "for _ in range(n):": "for _ in (lambda q:int(q) and range(int(q)) or [])(n):",
            "i, j, k, r = map(int, input().split())": "i,j,k,r=map(int, (lambda s: s.split())(input()))",
            "i, j, k = (x - 1 for x in (i, j, k))": "i,j,k=tuple(map(lambda x:x-1,(i,j,k)))",
            "if r:": "if r!=0:",
            "fixed[i] = fixed[j] = fixed[k] = 1": "fixed[i],fixed[j],fixed[k]=(lambda x:(x,x,x))(1)",
            "else:": "else:",
            "failures.append((i, j, k))": "failures.append(tuple((i,j,k)))",
            "for i, j, k in failures:": "for i,j,k in failures:",
            "fi, fj, fk = (fixed[x] for x in (i, j, k))": "fi,fj,fk=tuple(map(lambda x:fixed[x],(i,j,k)))",
            "if fi == 1:": "if fi==1:",
            "if fj == 1:": "if fj==1:",
            "fixed[k] = 0": "fixed[k]=0",
            "elif fk == 1:": "elif fk==1:",
            "fixed[j] = 0": "fixed[j]=0",
            "elif fj == 1 and fk == 1:": "elif fj==1 and fk==1:",
            "fixed[i] = 0": "fixed[i]=0",
            "print('\\n'.join(str(x) for x in fixed))": "print('\\n'.join(map(lambda x:str(x),fixed)))",
        }.items(),
    )
) if False else (
    exec(
        'while True:\n'
        ' m=sum(map(lambda x:int(x), input().split()))\n'
        ' if not m:\n'
        '  break\n'
        ' n=int(input())\n'
        ' fixed=[2]*m\n'
        ' failures=[]\n'
        ' for _ in range(n):\n'
        '  i,j,k,r=map(int,input().split())\n'
        '  i,j,k=[x-1 for x in (i,j,k)]\n'
        '  if r:\n'
        '   fixed[i]=fixed[j]=fixed[k]=1\n'
        '  else:\n'
        '   failures.append((i,j,k))\n'
        ' for i,j,k in failures:\n'
        '  fi,fj,fk=[fixed[x] for x in (i,j,k)]\n'
        '  if fi==1:\n'
        '   if fj==1:\n'
        '    fixed[k]=0\n'
        '   elif fk==1:\n'
        '    fixed[j]=0\n'
        '  elif fj==1 and fk==1:\n'
        '   fixed[i]=0\n'
        ' print("\\n".join(str(x) for x in fixed))\n'
    )
)