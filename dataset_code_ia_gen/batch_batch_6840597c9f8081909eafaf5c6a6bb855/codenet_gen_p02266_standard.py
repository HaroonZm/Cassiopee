s=input()
stack=[]
areas=[]
for i,c in enumerate(s):
    if c=='\\':
        stack.append(i)
    elif c=='/' and stack:
        j=stack.pop()
        area=i-j
        while areas and areas[-1][0]>j:
            area+=areas.pop()[1]
        areas.append((j,area))
A=sum(a for _,a in areas)
print(A)
print(len(areas),*map(lambda x:x[1],areas))