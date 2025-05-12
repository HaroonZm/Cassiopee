import re
while True:
    n,t=input().split()
    
    if t=='X':
        break
    
    if '_'in t:
        ans=s.split('_')
    else :
        ans=re.findall(r'[a-z]+|[A-Z][a-z]*',n)
        
    if t=='D':
        ans='_'.join(map(str.lower,ans))
    else :
        ans=''.join(map(str.capitalize,ans))
        if t=='L':
            ans=ans[0].lower()+ans[1:]
    
    print(ans)