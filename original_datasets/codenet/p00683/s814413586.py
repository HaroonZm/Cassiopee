for _ in [0]*int(input()):
    s=input()
    cur=0
    for _ in [0]*int(input()):
        c=input()
        if c=='forward word':
            while cur<len(s) and s[cur]==' ':cur+=1
            while cur<len(s) and s[cur]!=' ':cur+=1
        elif c=='delete char':s=s[:cur]+s[cur+1:]
        elif c=='backward word':
            while cur>0 and s[cur-1]==' ':cur-=1
            while cur>0 and s[cur-1]!=' ':cur-=1
        elif c=='forward char':cur=min(len(s),cur+1)
        elif c=='delete word':
            if s[cur:].count(' ') == len(s[cur:]): continue
            while cur<len(s) and s[cur]==' ':s=s[:cur]+s[cur+1:]
            while cur<len(s) and s[cur]!=' ':s=s[:cur]+s[cur+1:]
        elif c[0]=='i':
            c=c.split('"')[1]
            s=s[:cur]+c+s[cur:]
            cur+=len(c)
        elif 'backward char':cur=max(0,cur-1)
    print(s[:cur]+'^'+s[cur:])