s=input()
res=""
expect='A'
for c in s:
    if c==expect:
        res+=c
        expect='Z' if expect=='A' else 'A'
if len(res)>=2 and res[-1]=='Z':
    print(res)
else:
    print(-1)