s,a,c=input(),1,0
for x in s:
    if x=='A':a=0
    elif x=='Z' and not a:a,c=1,c+1
print('AZ'*c if c else -1)